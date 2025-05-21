const searchForm = document.querySelector('.search-form');
const productList = document.querySelector('.products-list');

searchForm.addEventListener('submit', async function(event){
    event.preventDefault();
    const inputValue = event.target[0].value;

    try {
        const response = await fetch(`https://api.mercadolibre.com/sites/MLB/search?q=${inputValue}`);
        
        if (!response.ok) throw new Error("Erro ao buscar dados");

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
