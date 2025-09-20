# encadrement-system
•	📌 Objectif du projet (application web + mobile pour encadrement).
	•	📌 Stack : Django REST + React/Next.js.
	•	📌 Organisation du repo (backend / frontend).
	•	📌 Règles Git :
	•	main = stable
	•	develop = intégration
	•	feature/* = travail en cours (PR obligatoire).
📂 Organisation du repo:

   encadrement-system/
     │── backend/        # Projet Django REST
     │   ├── config/     # Paramètres Django
     │   ├── students/   # Module de gestion des étudiants
     │   ├── users/      # Gestion des utilisateurs et rôles
     │   ├── venv/       # Virtualenv (non versionné)
     │   └── manage.py
     │
     │── frontend/       # Projet React/Next.js (bientôt)
     │── README.md
---

## ⚙️ Installation Backend (Django + PostgreSQL)

### 1. Cloner le repo
```bash
git clone https://github.com/<ton_repo>/encadrement-system.git
cd encadrement-system/backend

2. Créer un environnement virtuel:
 python3 -m venv venv
 source venv/bin/activate

3. Installer les dépendances:
 pip install -r requirements.txt

4. Configurer la base PostgreSQL:
 CREATE DATABASE encadrement;
 CREATE USER encadrement_user WITH PASSWORD  'encadrement_user';
 GRANT ALL PRIVILEGES ON DATABASE encadrement TO encadrement_user;
 GRANT ALL ON SCHEMA public TO encadrement_user;
 ALTER SCHEMA public OWNER TO encadrement_user;

Modifier backend/config/settings.py :

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'encadrement',
        'USER': 'encadrement_user',
        'PASSWORD': 'motdepassefort',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Appliquer les migrations:
 python manage.py makemigrations
 python manage.py migrate

6. Créer un superutilisateur:
 python manage.py createsuperuser

7. Lancer le serveur:
 python manage.py runserver
