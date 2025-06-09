$(document).ready(function(){

    const addedBooks = JSON.parse(localStorage.getItem('addedBooks')) || {};

    $('.add-to-book').each(function() {
        const book_id = $(this).data('book-id');
        if (addedBooks[book_id]) {
            $(this).text('Книга добавлена в прочитанное');
            $(this).attr('href', 'http://127.0.0.1:4000/mybooks/');
        }
    });

    $(document).on("click", ".add-to-book", function (e) {

        e.preventDefault();

        var book_id = $(this).data("book-id");
        var add_to_book_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_book_url,
            data: {
                book_id: book_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),},

            success: function (data) {
                
                $('#success-message').fadeIn().delay(3000).fadeOut();

                addedBooks[book_id] = true;
                localStorage.setItem('addedBooks', JSON.stringify(addedBooks));

                $('.add-to-book[data-book-id="' + book_id + '"]').text('Книга добавлена в прочитанное');
                $('.add-to-book[data-book-id="' + book_id + '"]').attr('href', 'http://127.0.0.1:4000/mybooks/');
            }
        })

    })
})