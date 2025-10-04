# Images Directory

This directory contains diagrams, screenshots, and other visual elements for the project documentation.

## Contents

### Architecture Diagrams

The main architecture diagram is included in the README.md using Mermaid syntax. For presentations or external use, you can:

1. **Generate PNG from Mermaid**: Use tools like [Mermaid Live Editor](https://mermaid.live/) to export diagrams
2. **Screenshot**: Capture the rendered diagram from GitHub
3. **Custom Diagrams**: Create additional diagrams using tools like:
   - draw.io / diagrams.net
   - Lucidchart
   - Excalidraw

### Suggested Visuals to Add

1. **architecture_overview.png**: High-level system architecture
2. **feature_flow.png**: Data flow from raw data to features
3. **batch_vs_online.png**: Comparison of batch and online serving patterns
4. **demo_output.png**: Screenshot of demo script output
5. **code_snippet.png**: Highlighted code examples

### Creating Diagrams

#### From Mermaid (in README.md)

1. Visit [Mermaid Live Editor](https://mermaid.live/)
2. Copy the Mermaid code from README.md
3. Paste into the editor
4. Export as PNG or SVG
5. Save to this directory

#### Custom Diagrams

Use any diagramming tool and save files here with descriptive names:
- Use PNG for screenshots and raster images
- Use SVG for vector graphics (preferred for diagrams)
- Keep file sizes reasonable (< 1MB per image)

### Naming Convention

Use descriptive, lowercase names with hyphens:
- `feature-store-architecture.png`
- `training-workflow.png`
- `serving-workflow.png`
- `demo-output-screenshot.png`

### Usage in Documentation

Reference images in markdown files using relative paths:

```markdown
![Architecture Diagram](./images/feature-store-architecture.png)
```

Or with alt text and title:

```markdown
![Feature Store Architecture](./images/architecture.png "Feature Store System Architecture")
```

### Image Guidelines

- **Resolution**: Use high-resolution images (at least 1920x1080 for diagrams)
- **Format**: PNG for screenshots, SVG for diagrams when possible
- **Size**: Optimize images to keep file sizes reasonable
- **Accessibility**: Always include descriptive alt text
- **Consistency**: Use consistent colors and styling across diagrams

### Tools Recommendations

**Diagramming**:
- [Mermaid](https://mermaid.js.org/) - Text-based diagrams (already used in README)
- [draw.io](https://app.diagrams.net/) - Free, web-based diagramming
- [Excalidraw](https://excalidraw.com/) - Hand-drawn style diagrams

**Screenshots**:
- Windows: Snipping Tool, Snip & Sketch
- Mac: Command + Shift + 4
- Linux: GNOME Screenshot, Flameshot

**Image Optimization**:
- [TinyPNG](https://tinypng.com/) - Compress PNG images
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - Optimize SVG files

## Current Status

This directory is currently a placeholder. Add visual assets as needed to enhance the documentation.
