document.addEventListener("DOMContentLoaded", function () {
  const itensPorPagina = 8;

  const tabelas = [
    { tabelaId: "produtos-tabela", itemClass: "produto-item", paginacaoId: "paginacao" },
  ];

  tabelas.forEach(({ tabelaId, itemClass, paginacaoId }) => {
    const tabela = document.getElementById(tabelaId);
    const paginacao = document.getElementById(paginacaoId);
    if (!tabela || !paginacao) return;

    const linhas = Array.from(tabela.getElementsByClassName(itemClass));
    if (linhas.length === 0) return;

    let paginaAtual = 1;
    const totalPaginas = Math.ceil(linhas.length / itensPorPagina);

    function mostrarPagina(pagina) {
      const inicio = (pagina - 1) * itensPorPagina;
      const fim = inicio + itensPorPagina;

      linhas.forEach((linha, index) => {
        linha.style.display = index >= inicio && index < fim ? "" : "none";
      });

      renderizarLinksPaginacao(pagina);
    }

    function renderizarLinksPaginacao(paginaAtual) {
      paginacao.innerHTML = "";

      for (let i = 1; i <= totalPaginas; i++) {
        const link = document.createElement("button");
        link.textContent = i;
        link.className = "btn btn-outline-primary btn-sm me-1";
        if (i === paginaAtual) {
          link.classList.add("active");
        }

        link.addEventListener("click", () => {
          mostrarPagina(i);
        });

        paginacao.appendChild(link);
      }
    }

    mostrarPagina(paginaAtual);
  });
});
