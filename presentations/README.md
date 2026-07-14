# Customer Success Mockups PowerPoint

## Descripción
Este repositorio contiene los scripts y recursos necesarios para generar presentaciones PowerPoint con mockups de Customer Success.

## Última Presentación Generada
**Fecha:** 14 de julio de 2026  
**Archivo:** Customer_Success_Mockups_Presentation.pptx  
**Rama:** mockup-customer-success-2026-07-14

## Contenido de la Presentación

### Slide 1
**Archivo:** V4_3.3.1.1_Customer_Success_Overview_Importe_menu.png  
**Descripción:** Vista general del menú de importe en Customer Success Overview

### Slide 2
**Archivo:** Prueba_2.png  
**Descripción:** Mockup con menú lateral expandido mostrando secciones de Overview, Comercial, Customer Success y Producto

### Slide 3
**Archivo:** Prueba_3.png  
**Descripción:** Vista completa del dashboard de Customer Success con métricas y gráficos

## Estructura del Proyecto

```
.
├── presentations/
│   └── generate_powerpoint.py    # Script para generar el PowerPoint
├── images/                         # Carpeta para mockups (no incluida en repo)
│   ├── V4_3.3.1.1_Customer_Success_Overview_Importe_menu.png
│   ├── Prueba_2.png
│   └── Prueba_3.png
└── README.md
```

## Requisitos

- Python 3.7+
- python-pptx

## Instalación

```bash
pip install python-pptx
```

## Uso

1. Coloca las imágenes de los mockups en el mismo directorio que el script
2. Ejecuta el script:

```bash
python presentations/generate_powerpoint.py
```

3. El archivo `Customer_Success_Mockups_Presentation.pptx` será generado en el directorio actual

## Características

- Formato 16:9 (10" x 5.625")
- Cada mockup ocupa toda la diapositiva
- Sin márgenes ni bordes
- Orden personalizable de las diapositivas

## Notas

- Las imágenes deben estar en formato PNG
- El script busca las imágenes en el directorio de trabajo actual
- Se puede modificar el orden de las diapositivas editando la lista `images` en el script

## Contacto

Para más información o soporte, contacta al equipo de Customer Success.
