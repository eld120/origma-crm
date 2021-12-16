/* Project specific Javascript goes here. */

//Form validation
const event = document.addEventListener('click')
const customerForm =  document.querySelector('#customer-form')


async function getTestData(endpoint){
    try {
        const query = await fetch(endpoint)
        const payload = query.text()
    }
    catch(error) {
        console.log('problem:', error)
    }

    console.log(payload)


}


async function setAddressLocation(customerId) {
    const sessionCookie = fetch()

}
