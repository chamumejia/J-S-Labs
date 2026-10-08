# Guía de contribución

Esta guía establece cómo Jacob y Samuel trabajan en el proyecto, organizan sus cambios y revisan el código. Se aplica a todas las contribuciones del repositorio.

## Ramas

La rama `main` contiene la versión estable del proyecto. No se deben realizar cambios directamente sobre `main`; todos los cambios se trabajan en una rama y se integran mediante un Pull Request (PR).

Crear una rama nueva desde la última versión de `main` para cada tarea. Usar minúsculas, separar las palabras con guiones y comenzar con uno de estos prefijos:

- `feature/`: agregar una funcionalidad. Ejemplo: `feature/inicio-sesion`.
- `fix/`: corregir un error. Ejemplo: `fix/error-validacion`.
- `docs/`: modificar documentación. Ejemplo: `docs/guia-contribucion`.
- `refactor/`: reorganizar código sin cambiar el comportamiento. Ejemplo: `refactor/ordenar-servicios`.
- `test/`: agregar o modificar pruebas. Ejemplo: `test/pruebas-registro`.
- `chore/`: realizar tareas de mantenimiento o configuración. Ejemplo: `chore/actualizar-dependencias`.

## Commits

Escribir mensajes de commit breves y claros, en minúsculas, con este formato:

`tipo: descripcion del cambio`

Usar uno de estos tipos:

- `feat`: nueva funcionalidad.
- `fix`: corrección de un error.
- `docs`: documentación.
- `refactor`: reorganización del código sin cambiar su comportamiento.
- `test`: pruebas.
- `chore`: configuración o mantenimiento.

Redactar la descripción en presente, sin punto final. Ejemplos:

- `docs: agrega guia de contribucion`
- `feat: agrega formulario de registro`
- `fix: valida campos obligatorios`

## Pull Requests

Al terminar una tarea, abrir un PR desde la rama de trabajo hacia `main`. Cada PR debe:

- Tener un título claro que describa el cambio.
- Explicar qué se cambió y por qué.
- Indicar las pruebas realizadas y sus resultados.
- Incluir capturas de pantalla si modifica la interfaz.
- Mantenerse enfocado en una tarea; los cambios no relacionados deben ir en otro PR.

## Revisión del código

Jacob y Samuel se revisan mutuamente los PR. La persona que crea el PR no puede aprobarlo; la otra persona debe revisarlo y dejar su aprobación antes de integrarlo.

Quien revisa debe comprobar que el cambio cumple su objetivo, que el código es claro y coherente con el proyecto, que no incluye cambios ajenos a la tarea y que no expone contraseñas, claves ni datos personales. También debe verificar que la documentación y las pruebas se hayan actualizado cuando el cambio las afecte.

Las observaciones solicitadas deben resolverse antes de fusionar el PR. Si hay desacuerdo sobre una decisión técnica, Jacob y Samuel deben conversar y acordar una solución antes de integrarlo.

## Pruebas y aprobación

Antes de solicitar revisión, quien crea el PR debe ejecutar las pruebas automatizadas disponibles para el proyecto y comprobar que pasan. Si todavía no hay pruebas automatizadas para la parte modificada, debe realizar una comprobación manual y describir en el PR qué verificó.

Un PR se puede fusionar a `main` cuando:

1. Tiene la aprobación de la otra persona del equipo.
2. Las observaciones importantes de la revisión están resueltas.
3. Las pruebas automatizadas pasan o se documentó la comprobación manual cuando no existen pruebas para ese cambio.
4. No tiene conflictos pendientes con `main`.

Después de fusionar el PR, se puede eliminar la rama de trabajo.
