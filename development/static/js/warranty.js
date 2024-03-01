const addMoreBtn = document.getElementById('add-more');
const formContainer = document.getElementById('form-container');
const emptyForm = document.getElementById('empty-form');
const totalNewForms = document.getElementById('id_partsrequired_set-TOTAL_FORMS');

addMoreBtn.addEventListener('click', addNewForm);

function addNewForm() {
    // Clone the empty form
    const newForm = emptyForm.cloneNode(true);
    newForm.style.display = 'block';

    // Update the form's index to match the next form in the formset
    const formIndex = parseInt(totalNewForms.value);
    const formId = `id_partsrequired_set-${formIndex}-`;
    const formInputs = newForm.getElementsByTagName('input');
    for (let i = 0; i < formInputs.length; i++) {
        formInputs[i].id = formInputs[i].id.replace('__prefix__', formIndex);
        formInputs[i].name = formInputs[i].name.replace('__prefix__', formIndex);
    }

    // Add the new form to the form container
    formContainer.appendChild(newForm);

    // Update the total number of forms
    totalNewForms.value = formIndex + 1;
}