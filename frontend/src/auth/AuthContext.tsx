import { createContext, useState, useEffect, useContext } from "react";
import api from "../services/api";

export type User = {
  id: number;
  username: string;
  password: string;
  role: "kepsek" | "guru" | "tu" | "bendahara" | "SUPERADMIN";
};

type AuthContextType = {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
};

export const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const login = async (username: string, password: string) => {
    try {
      const res = await api.post("/auth/login/", { username, password });

      // 1. Simpan ke LocalStorage
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      localStorage.setItem("role", res.data.role);

      // 2. SET TOKEN KE AXIOS SECARA MANUAL (Penting!)
      // Agar request setelah ini tidak perlu nunggu refresh halaman
      api.defaults.headers.common['Authorization'] = `Bearer ${res.data.access}`;

      setUser(res.data.user);

      // 3. Redirect atau beri notifikasi sukses
      console.log("Login sukses, token disimpan");
    } catch (err) {
      console.error("Login gagal:", err);
      alert("Username atau password salah");
    }
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  const loadUser = async () => {
    try {
      const res = await api.get("/auth/me/");
      setUser(res.data);
    } catch {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    // ⬅️ HANYA loadUser JIKA ADA TOKEN
    if (localStorage.getItem("access")) {
      loadUser();
    } else {
      setLoading(false);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth harus dipakai di dalam AuthProvider");
  }
  return context;
}
