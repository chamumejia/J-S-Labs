# Bitácora — Jacob Cardona

1. Qué hice: contribuí al README y a CONTRIBUTING.md en el PR #7, y agregué mi perfil en equipo/jacob.md con el PR #8; mi rol es apoyar la documentación y el desarrollo.
2. Qué me pidieron mejorar: en los PR #7 y #8 no aparecen solicitudes de cambios; ambos fueron aprobados y en el #8 recibí el comentario “muy bonito”.
3. Qué pedí mejorar a mi compañero: en las revisiones registradas de los PR #6 y #10 dejé aprobaciones, pero no pedí una mejora; debo completar ese paso en una revisión real según la guía.
4. Uso de IA: le pedí a Zapia comparar el repositorio con la guía.
5. Qué cambié y por qué: contrasté el borrador con README.md, CONTRIBUTING.md y el historial de PR; añadí mi rol y mis tareas y aclaré que no hubo solicitudes de cambios para no inventar información.

## R1 — Pedidos de Rápido Paisa

1. Ticket: trabajé el issue #18 creando `src/organizar.py` para organizar los pedidos por sede.
2. Problema y solución: algunos archivos no se podían clasificar; los dejé en `revisar/` y copié los pedidos reconocidos a sus carpetas, sin mover los originales.
3. Prueba: obtuve 87 pedidos en Itagüí, 75 en Envigado, 88 en Sabaneta y 17 para revisar; confirmé que `bandeja_entrada/` quedó intacta y el PR #21 se fusionó.
4. Uso de IA: le pedí a Zapia ayuda para implementar y probar el organizador; me sugirió usar `obtener_sede()` y `shutil.copy()`.
5. Corrección: al revisar la orientación, encontré que `.gitignore` en `main` tenía texto descriptivo en vez de reglas; reabrí el issue #16 y propuse corregirlo en el PR #22, pendiente de revisión.
6. Qué ajusté: mantuve la copia para conservar los originales y agregué las reglas de exclusión reales para que Git ignore los datos generados.
