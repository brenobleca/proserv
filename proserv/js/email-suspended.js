document.querySelectorAll('form[data-email-suspended]').forEach(function (form) {
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        event.stopImmediatePropagation();
        window.alert('O envio por e-mail está temporariamente suspenso. Para continuar, use o WhatsApp.');
    }, true);
});

document.querySelectorAll('form[data-whatsapp-number]').forEach(function (form) {
    var whatsappLink = form.querySelector('[data-whatsapp-send]');

    whatsappLink.addEventListener('click', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            form.reportValidity();
            return;
        }

        var message = [
            'Olá! Gostaria de entrar em contato com a Proserv Systems.',
            '',
            'Nome: ' + form.elements.namedItem('nome').value.trim(),
            'E-mail: ' + form.elements.namedItem('email').value.trim(),
            'Cidade: ' + form.elements.namedItem('cidade').value.trim(),
            'Telefone: ' + form.elements.namedItem('tel').value.trim(),
            '',
            'Mensagem: ' + form.elements.namedItem('msg').value.trim()
        ].join('\n');

        whatsappLink.href = 'https://wa.me/' + form.dataset.whatsappNumber
            + '?text=' + encodeURIComponent(message);
    });
});
