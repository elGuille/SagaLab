# Contexto para Claude Code

Carpeta de trabajo de un **plan personal según el Método Harada**. No es código: son
documentos para rellenar, más una herramienta local (`tracker.html`).

## Qué es cada cosa

`README.md` explica el método y el orden. Las piezas van `01`–`06`; `07` es un anexo
(los trece principios de Sam Altman traducidos a candidatos de pilar y de casilla).

**El orden de numeración no es el orden de llenado.** Se empieza por `02` (análisis del
pasado), luego `01` (objetivo), luego `03` (carta de 64), luego `04` (rutinas). Si el usuario
pide "empezar el plan", empieza por `02`.

## Cómo ayudar aquí

- **Rellenar, no reescribir.** Los archivos son plantillas con huecos (`>`, tablas vacías,
  `____`). El trabajo normal es completarlos con el contenido del usuario, conservando la
  estructura y las notas explicativas.
- **Entrevista antes de escribir.** No inventes objetivos, valores ni análisis del pasado —
  son datos personales que solo tiene el usuario. Pregunta.
- **La carta de 64 es donde más aportas.** Las casillas 6, 7 y 8 de cada pilar son las que no
  salen solas. Criterio para cada acción: *debe poder empezarse mañana sin permiso de nadie.*
  Nada de "mejorar mi inglés"; sí "20 min de shadowing con el podcast X, a las 7:30".
- **El diario (`05`) es del usuario.** No lo edites ni lo resumas salvo petición explícita.

## `tracker.html`

Una sola página autocontenida: sin build, sin red, sin dependencias. Persiste en
`localStorage` bajo la clave `harada.v1`. Si lo tocas, mantén esas propiedades y prueba en un
navegador de verdad — la rejilla 9×9 replica cada pilar al centro de su bloque exterior y esa
correspondencia se rompe con facilidad.

## Privacidad

Esta carpeta nació en el repositorio de un sitio publicado en GitHub Pages. Si sigue ahí,
**no la fusiones a la rama principal**: quedaría accesible en internet. Lo suyo es que viva en
un repositorio privado. Ver el aviso al principio del `README.md`.
