document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('estoqueChart').getContext('2d');

  const estoqueChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: window.nomes_produtos,
      datasets: [{
        label: 'Estoque',
        data: window.valores_estoque,
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
});
