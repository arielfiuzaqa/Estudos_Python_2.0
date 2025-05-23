document.addEventListener("DOMContentLoaded", () => {
  const searchForm = document.querySelector('.search-form');
  const productList = document.querySelector('.product-list');

  if (!searchForm || !productList) {
    console.error("Elemento '.search-form' ou '.product-list' não encontrado.");
    return;
  }

  searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const inputValue = event.target[0].value.trim();

    if (!inputValue) {
      productList.innerHTML = `<p style="color: orange;">Digite um termo para buscar.</p>`;
      return;
    }

    try {
      const response = await fetch(`https://api.mercadolibre.com/sites/MLB/search?q=${encodeURIComponent(inputValue)}`);

      if (!response.ok) {
        throw new Error(`Erro ${response.status}: ${response.statusText}`);
      }

      const json = await response.json();
      const products = json?.results?.slice(0, 10) || [];

      displayItens(products);
    } catch (error) {
      console.error("Erro na requisição:", error);
      productList.innerHTML = `<p style="color: red;">Erro ao buscar produtos. Tente novamente.</p>`;
    }
  });

  function displayItens(products) {
    if (products.length === 0) {
      productList.innerHTML = `<p>Nenhum produto encontrado.</p>`;
      return;
    }

    productList.innerHTML = products.map(product => `
      <div class="product-card">
        <img src="${product.thumbnail}" alt="${product.title}">
        <h3>${product.title}</h3>
        <p>R$ ${product.price}</p>
        <p>Loja: ${product.seller?.nickname || 'Desconhecida'}</p>
      </div>
    `).join('');
  }
});
