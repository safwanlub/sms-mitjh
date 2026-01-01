import { Navigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function RoleRoute({
  allow,
  children,
}: {
  allow: string[];
  children: JSX.Element;
}) {
  const { user } = useAuth();

  if (!user) return <Navigate to="/login" replace />;
  if (!allow.includes(user.role)) return <Navigate to="/login" replace />;

  return children;
}
