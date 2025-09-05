# Overview

This is a personal blog website built with Pelican, a Python-based static site generator. The site belongs to Sarah Rogue and serves as a platform for sharing technical content, particularly focused on GNU/Linux topics. The blog generates static HTML files from content written in markup languages and deploys to GitHub Pages at sarah-rogue.me.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Static Site Generation
The project uses Pelican as the core static site generator, which converts content files into a complete static website. This architecture choice provides fast loading times, security benefits, and easy hosting on static file servers.

## Content Management
- **Source Content**: Blog posts and pages are written in markup format (likely Markdown or reStructuredText) and stored in the `content/` directory
- **Output Generation**: Static HTML files are generated into the `docs/` directory, which serves as the publication folder
- **Build Process**: Uses Python-based Pelican engine with custom configuration for site generation

## Configuration Architecture
- **Base Configuration**: `pelicanconf.py` contains development settings including site metadata, paths, and basic features
- **Production Configuration**: `publishconf.py` extends base config with production-specific settings like the live site URL and feed generation
- **Task Automation**: `tasks.py` implements Invoke-based build automation for common operations like cleaning, building, and serving

## Deployment Strategy
- **Static Hosting**: Targets GitHub Pages deployment with the `docs/` folder as the publication directory
- **Domain Configuration**: Uses custom domain `sarah-rogue.me` for the live site
- **Build Automation**: Includes automated commit messaging and branch management for GitHub Pages

## Theme and Presentation
- **Minimal Theme**: Uses a basic HTML theme with semantic markup
- **Responsive Design**: Includes viewport meta tags for mobile compatibility
- **Social Integration**: Configured for Twitter/X social media links
- **Branding**: Custom avatar, site subtitle, and personal branding elements

## Content Organization
- **Categories**: Supports content categorization (e.g., "GNU-Linux")
- **Archives**: Automatic generation of chronological content archives
- **Authors**: Multi-author support (though currently single-author)
- **Pagination**: Configured for 4 posts per page

# External Dependencies

## Core Framework
- **Pelican**: Python-based static site generator for content processing and HTML generation
- **Python**: Runtime environment for the build system

## Build Tools
- **Invoke**: Python task execution library for build automation and deployment tasks

## Hosting and Deployment
- **GitHub Pages**: Static site hosting platform
- **Custom Domain**: sarah-rogue.me domain configuration

## Content Format Support
- **Markup Languages**: Support for Markdown and/or reStructuredText content authoring

## Social Media Integration
- **Twitter/X**: Social media profile linking and potential content sharing

## Development Dependencies
- **HTTP Server**: Built-in development server for local testing and preview