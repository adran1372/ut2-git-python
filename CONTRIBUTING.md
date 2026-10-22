# Cómo contribuir a este proyecto
## Flujo de ramas
Nunca se trabaja directamente sobre `main`. Para cada cambio se crea una
rama nueva a partir de `main` (`git switch -c alterno`).
## Mensajes de commit
Se sigue el formato `tipo: descripción`, con los tipos `feat`, `fix`,
`docs`, `style`, `refactor`, `test` y `chore`
1. Crea una rama desde `main`.
2. Haz tus commits en ella.
3. Sube la rama: `git push -u origin alterno`.
4. Abre una Pull Request en GitHub describiendo el cambio.
5. Espera la revisión antes de fusionar.
## Cómo clonar y ejecutar este proyecto
git clone git@github.com:adran1372/ut2-git-python.git
cd ut2-git-python
python3 ej01_par_impar.py # (python en Windows)
