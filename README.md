# 🚀 Utilitaires Python

<p align="center">
  <b>Une boîte à outils simple et puissante pour automatiser ton quotidien</b><br>
  File management • Logging avancé • Envoi d'emails
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg">
  <img src="https://img.shields.io/badge/license-MIT-green.svg">
  <img src="https://img.shields.io/badge/status-active-success.svg">
  <img src="https://img.shields.io/badge/contributions-welcome-orange.svg">
</p>

---

## ✨ Aperçu

Ce projet regroupe plusieurs classes utilitaires pour simplifier le développement :

* 📁 Gestion intelligente des fichiers
* 📝 Logging avancé et lisible
* 📧 Envoi d’emails automatisé

---

## 🧰 Modules

| Module         | Description                              |
| -------------- | ---------------------------------------- |
| 📂 FileManager | Gestion avancée des fichiers et dossiers |
| 📝 ProLogger   | Logger personnalisable avec couleurs     |
| 📧 EmailSender | Envoi d’emails avec pièces jointes       |

---

## 📂 FileManager

> Simplifie toutes les opérations sur fichiers

### 🚀 Features

* Création automatique de dossiers
* Renommage intelligent
* Copie / déplacement
* Gestion des conflits (overwrite ou auto rename)

### 💻 Exemple

```python
from utilis import FileManager

fm = FileManager(overwrite=False, auto_rename=True)

fm.ensure_dir("output")

new_file = fm.rename("test.txt", "renamed.txt")

fm.transfer(new_file, "output/", mode="copy")
```

---

## 📝 ProLogger

> Un logger propre, lisible et configurable

### 🚀 Features

* Console + fichiers
* Logs colorés 🌈
* Multi-niveaux (info, warning, error)
* Facile à intégrer

### 💻 Exemple

```python
from services import ProLogger

logger = ProLogger(
    name="my_app",
    log_dir="logs",
    console=True,
    colored=True
).get()

logger.info("App started")
logger.warning("Watch out")
logger.error("Boom")
```

---

## 📧 EmailSender

> Envoi d’emails simple et rapide

### 🚀 Features

* Support Gmail
* CC / BCC
* Pièces jointes 📎
* Connexion sécurisée

### 💻 Exemple

```python
from services import EmailSender

sender = EmailSender(
    provider="gmail",
    email="tonemail@gmail.com",
    password="mot_de_passe_application"
)

sender.connect()

sender.send_email(
    to=["a@gmail.com"],
    cc=["b@gmail.com"],
    bcc=["c@gmail.com"],
    subject="Test CC/BCC",
    content="Hello",
    attachments=["doc.pdf"]
)

sender.close()
```

---

## 🔐 Sécurité

⚠️ Important :

* Ne jamais utiliser ton mot de passe principal
* Utilise un **mot de passe d’application**
* Active le 2FA (authentification à deux facteurs)

---


## ⭐ Support

Si ce projet t’aide :

👉 Laisse une ⭐ sur GitHub
👉 Partage le projet

---

<p align="center">
  Fait avec ❤️ en Python
</p>
