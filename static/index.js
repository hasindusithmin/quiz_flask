
fetch('/quiz')
    .then(res=>res.json())
    .then(data=>{
        for (const {question,answer,options,id} of data) {
            const li = document.createElement('li')
            li.className = 'w3-card-4'
            const div = document.createElement('div')
            div.innerHTML = question
            const opts = options.split(',')
            const select = document.createElement('select')
            select.className = 'w3-input'
            for (const opt of opts) {
                const option = document.createElement('option')
                option.innerText = opt
                option.value = opt
                select.appendChild(option)
            }
            li.appendChild(div)
            li.appendChild(select)
            document.getElementById('root').appendChild(li)
        }
    })