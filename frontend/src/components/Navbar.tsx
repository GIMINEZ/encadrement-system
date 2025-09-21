"use client";
import Link from "next/link";
import { logout } from "../lib/auth";
import { useRouter } from "next/navigation";

export default function Navbar() {
  const router = useRouter();

  const handleLogout = () => {
    logout();
    router.push("/login");
  };

  return (
    <nav style={{ padding: 10, background: "#eee" }}>
      <Link href="/profile">Profil</Link> |{" "}
      <Link href="/dashboard">Admin</Link> |{" "}
      <button onClick={handleLogout}>Déconnexion</button>
    </nav>
  );
}