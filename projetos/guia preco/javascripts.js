const searchForm = document.querySelector('.search-form');
const productList = document.querySelector('.products-list');
searchForm.addEventListener('submit', async function(event){
    event.preventDefault()
    const inputValue = event.target[0].value

    const data = await fetch(`https://api.mercadolibre.com/sites/MLB/search?q=${inputValue}`)
    const products = (await data.json()).results.slice(0, 10)

    displayItens(products) 
});

function displayItens(products) {
    productList.innerHTML = products.map( products => `
        <div class="product-card">
            <img src="${products.thumbnail}" alt="${products.title}">
            <h3>${products.title}</h3>
            <p>R$ ${products.price.toLocaleString('pt-br', {style: "currency", currency: "BRL"})}</p>
            <p>Loja: ${product.seller.nickname}</p>
        
        </div>
    `).join('')
}