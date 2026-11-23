# Goulart InfoSolutions

Site e identidade visual da Goulart InfoSolutions: serviços de TI por alocação para empresas e terceirizadoras (escalonamento técnico, configuração de ambientes, backup e gestão de acessos).

Site estático, sem build e sem chamadas externas. Fontes hospedadas no próprio repositório.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `index.html` | Site de uma página |
| `assets/css/tokens.css` | Tokens de marca (cor, tipo, escala). Fonte única para site e manual |
| `assets/css/site.css` | Estilos do site |
| `assets/js/config.js` | **Contato comercial.** Único arquivo a editar para trocar e-mail e WhatsApp |
| `assets/fonts/` | Chakra Petch e IBM Plex Sans (licença OFL) |
| `brand/manual.html` | Manual de marca: logotipo, cor, tipografia, voz, aplicações |
| `brand/logo/` | Logotipos em SVG (textos já em curvas): horizontal, monograma, claro, escuro, uma cor, favicon |
| `brand/png/` | PNG prontos: logotipos, favicons, preview social, banner do LinkedIn |
| `brand/applications/` | Fontes HTML do preview social, do banner e da assinatura de e-mail |
| `tools/` | Scripts que regeneram os SVG e os PNG |

## Publicar no GitHub Pages

1. No GitHub, abra **Settings > Pages**.
2. Em **Build and deployment**, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)`.
3. O site fica em `https://leandrogoulart.github.io/GoulartInfoSolutions/`.

Se usar domínio próprio, troque as duas URLs absolutas (`og:image` e `og:url`) no `<head>` do `index.html` e a URL do logotipo em `brand/applications/assinatura-email.html`.

## Regenerar logotipo e PNG

```bash
cd tools
npm install
python3 -m pip install fonttools playwright && python3 -m playwright install chromium
python3 make_logo.py   # SVG do logotipo, em ../brand/logo/
python3 gen_png.py     # PNG, em ../brand/png/ e ../assets/img/
```

## Pendências antes de divulgar

- [ ] Registrar domínio e consultar o INPI por "Goulart InfoSolutions". "InfoSolutions" é nome comum; confirme antes de investir em material impresso.
- [ ] Incluir o CNPJ no rodapé. Terceirizadoras costumam conferir.
- [ ] Trocar o e-mail pessoal por um e-mail do domínio da empresa e atualizar `config.js`, a assinatura e o `index.html`.
- [ ] Revisar a seção "Contratação": se houver modelo de NDA ou condições de faturamento, acrescentar.
- [ ] Conferir cada serviço listado em `index.html` contra o que você realmente entrega hoje.
