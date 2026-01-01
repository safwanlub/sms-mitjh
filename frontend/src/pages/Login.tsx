import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../auth/AuthContext";

export default function Login() {
  const { login, user } = useContext(AuthContext);
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const redirectByRole = (role: string) => {
    switch (role) {
      case "kepsek":
        return "/kepsek";
      case "guru":
        return "/guru";
      case "tu":
        return "/tu/siswa";
      case "bendahara":
        return "/bendahara/keuangan";
      default:
        return "/login";
    }
  };

  // ✅ REDIRECT SETELAH USER TERISI
  useEffect(() => {
    if (user?.role) {
      navigate(redirectByRole(user.role), { replace: true });
    }
  }, [user, navigate]);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      await login(username, password);
      // ⛔ jangan navigate di sini
    } catch {
      setError("Username atau password salah");
    }
  };

  return (
    <form onSubmit={submit} className="max-w-sm mx-auto mt-32 space-y-4">
      <h2 className="text-xl font-bold text-center">Login</h2>

      {error && <p className="text-red-600 text-sm">{error}</p>}

      <input
        className="w-full border px-3 py-2 rounded"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        className="w-full border px-3 py-2 rounded"
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className="w-full bg-blue-600 text-white py-2 rounded">
        Login
      </button>
    </form>
  );
}
