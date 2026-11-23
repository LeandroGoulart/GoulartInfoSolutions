(function () {
  var c = window.GIS_CONTACT || {};
  var email = document.querySelector('[data-contact="email"]');
  if (email && c.email) {
    email.href = "mailto:" + c.email + "?subject=" + encodeURIComponent("Proposta Goulart InfoSolutions");
  }
  var wa = document.querySelector('[data-contact="whatsapp"]');
  if (wa && /^\d{12,13}$/.test(c.whatsapp || "")) {
    wa.href = "https://wa.me/" + c.whatsapp + "?text=" + encodeURIComponent("Olá, vim pelo site da Goulart InfoSolutions.");
    wa.rel = "noopener";
    wa.hidden = false;
  }
  var ano = document.querySelector("[data-ano]");
  if (ano) ano.textContent = new Date().getFullYear();
})();
