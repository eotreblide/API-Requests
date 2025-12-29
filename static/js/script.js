const sendBtn = document.getElementById("sendBtn")
const url = document.getElementById("url")
const meth = document.getElementById("method")
const txt = document.getElementById("result")
const params = document.getElementById("jsonParams")
async function send() {
    try {
        const form = new FormData()
        form.append("u", url.value)
        form.append("m", meth.value)
        form.append("p", params.value)
        let res = await fetch("/request", {
            method: "POST",
            body: form
        })
        const data = await res.json()
        txt.textContent = data
    } catch {
        txt.textContent = `Ha ocurrido un error, porfavor revise si el metodo ${meth.value} es el correcto, si la api existe y si el json esta bien`
    }
}

sendBtn.addEventListener('click', send)
