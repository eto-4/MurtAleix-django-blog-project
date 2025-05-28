# Projecte Blog

## Introducció

Aquest projecte és un **blog web desenvolupat amb Django**, com a part del mòdul de Programació del cicle de Desenvolupament d'Aplicacions Web (DAW). L’objectiu és posar en pràctica els coneixements apresos sobre rutes, models, vistes, plantilles HTML, formularis, tests i desplegament local.

L’usuari pot veure els posts publicats, filtrar per etiquetes o autors, i accedir als detalls de cada entrada. El panell d’administració permet afegir, modificar o eliminar publicacions, autors i etiquetes.

---

# Instal·lació ràpida

## 1. Clonar el repositori


```bash
git clone https://github.com/EL_TEU_USUARI/projecte-blog.git
cd projecte-blog
```


## 2. Instal·lar les dependències
```bash
pip install -r requirements.txt
```

## 3. Executar migracions (La primera linia només en cas de que s'hagin fet canvis en les taules)
```bash
python manage.py makemigrations blog
python manage.py migrate
```

---

# Execució del projecte

## 1. Executar el servidor local
```bash
python manage.py runserver
```

## 2. Accedir a l’aplicació
### Obre el navegador i visita:
### http://127.0.0.1:8000/

---

# Altres detalls útils

## Panell d'administració:
### http://127.0.0.1:8000/admin/
### Usuari: Aleix
### Contrasenya: Admin

---

# Pàgina amb pydoc de Blog
## Consulta la documentació generada automàticament amb Pydoc a través de GitHub Pages:
[Veure documentació online](https://eto-4.github.io/MurtAleix-django-blog-project/)
