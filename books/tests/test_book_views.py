from django.test import TestCase
from django.urls import resolve, reverse
from books import views
from books.models import Category, Book, User
from unittest import skip


class bookViewsTest(TestCase):
    def test_book_home_view_function_is_correct(self):
        view = resolve(reverse('books:home'))
        self.assertIs(view.func, views.home)

    # 1
    @skip("WIP")
    def test_book_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('books:home'))
        self.assertEqual(response.status_code, 200)

    # 2
    @skip("WIP")
    def test_book_home_view_loads_correct_template(self):
        response = self.client.get(reverse('books:home'))
        self.assertTemplateUsed(response, 'books/pages/home.html')

    # 3
    @skip("WIP")
    def test_book_home_template_shows_no_books_found_if_no_books(self):
        response = self.client.get(reverse('books:home'))
        self.assertIn(
            '<h1>No books found here 🥲</h1>',
            response.content.decode('utf-8')
        )

    def test_book_category_view_function_is_correct(self):
        view = resolve(
            reverse('books:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_book_category_view_returns_404_if_no_books_found(self):
        response = self.client.get(
            reverse('books:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_book_detail_view_function_is_correct(self):
        view = resolve(
            reverse('books:book', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.book)

    def test_book_detail_view_returns_404_if_no_books_found(self):
        response = self.client.get(
            reverse('books:book', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)


    def test_recipe_home_template_loads_books(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        book = Book.objects.create(
            category=category,
            author=author,
            title='Título do Livro',
            description='Descrição do livro',
            slug='book-slug',
            publication_year = "1980",
            conservation_state = "U",
            language = "português",
            publishing_company = "editora",
            isbn = '1234',
            review = "review",
            review_is_html = True,            
            is_published = True,
            phoneNumber = "+234343433434",
            email = "rafael@gmail.com",       
        )    
        response = self.client.get(reverse('books:home'))
        content = response.content.decode('utf-8')
        response_context_books = response.context['books']
        self.assertIn('Título do Livro', content)
        self.assertIn('Descrição do livro', content)
        self.assertEqual(len(response_context_books), 1)
