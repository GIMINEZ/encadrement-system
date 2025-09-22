"use client";
import { useEffect, useState } from "react";
import api from "../../lib/api";
import { Student } from "../../types/student";

export default function ProfilePage() {
  const [student, setStudent] = useState<Student | null>(null);

  useEffect(() => {
    api.get("/students/").then((res) => {
      if (res.data.length > 0) {
        setStudent(res.data[0]); // l’élève ne voit que ses propres données
      }
    });
  }, []);

  if (!student) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Mon Profil</h1>
      <p><b>Matricule :</b> {student.matricule}</p>
      <p><b>Nom :</b> {student.nom}</p>
      <p><b>Prénom :</b> {student.prenom}</p>
      <p><b>Nationalité :</b> {student.nationalite}</p>
    </div>
  );
}