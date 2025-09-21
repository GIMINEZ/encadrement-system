"use client";
import { useEffect, useState } from "react";
import api from "../../lib/api";
import { Student } from "../../types/student";

export default function DashboardPage() {
  const [students, setStudents] = useState<Student[]>([]);

  useEffect(() => {
    api.get("/students/").then((res) => setStudents(res.data));
  }, []);

  return (
    <div>
      <h1>Tableau de bord - Admin</h1>
      <table border={1} cellPadding={5}>
        <thead>
          <tr>
            <th>Matricule</th>
            <th>Nom</th>
            <th>Prénom</th>
            <th>Nationalité</th>
          </tr>
        </thead>
        <tbody>
          {students.map((s) => (
            <tr key={s.id}>
              <td>{s.matricule}</td>
              <td>{s.nom}</td>
              <td>{s.prenom}</td>
              <td>{s.nationalite}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}