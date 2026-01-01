import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "./AuthContext";

export default function ProtectedRoute({
  children,
  role,
}: {
  children: JSX.Element;
  role?: string;
}) {
  const { user, loading } = useContext(AuthContext);

  // ⏳ Tunggu sampai loading selesai
  if (loading) {
    return <p>Loading...</p>;
  }

  // ❌ Belum login
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // ❌ Role tidak sesuai
  if (role && user.role !== role) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
