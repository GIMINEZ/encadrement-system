"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { login } from "../../lib/auth";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      await login(username, password);
      router.push("/profile"); // redirige vers profil après login
    } catch {
      alert("Erreur de connexion");
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "auto" }}>
      <h1>Connexion</h1>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
}