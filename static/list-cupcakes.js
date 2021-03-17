async function fetchCupcakes(){
    const res = await axios.get('/api/cupcakes');

    return res;
}

async function addCupcake(data){
    const res = await axios.post('/api/cupcakes', data)

    return res;
}

const appendCupcake = (cupcake) => {
    $('#cupcakes-list').append(`<li class="list-group-item">
    <small class="lead capitalize d-block">${cupcake.flavor}</small>
    <small class="capitalize d-block">Size: <small class="fw-bold">${cupcake.size}</small></small>
    <small class="capitalize d-block">Rating: <small class="fw-bold">${cupcake.rating}</small></small>
    <img src="${cupcake.image}" height="100" width="100" class="d-block">
    </li>`)
}

$(async function(){
    const res = await fetchCupcakes()
    cupcakes = res.data.cupcakes
    if(cupcakes){
        $('#cupcakes-div').append('<ul id="cupcakes-list" class="list-group list-group-horizontal my-3"></ul>')
        for(cupcake of cupcakes){
            appendCupcake(cupcake)
        }
    }else{
        $('#cupcakes-div').append('<h3 class="display-1">No Cupcakes!</h3>')
    }
})

$('#cupcake-form').on('submit', async function(evt){
    evt.preventDefault();
    const data = Object()
    const inputs = $('.form-control').toArray()

    inputs.forEach((inp) => data[$(inp).attr('name')] = $(inp).val())

    cupcake = await addCupcake(data)

    appendCupcake(cupcake.data.cupcake)

    return cupcake
})

