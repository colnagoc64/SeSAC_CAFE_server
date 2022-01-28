from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from board.models import Board


def boardList(request):
    if request.session.get('user') is not None:
        print('boardList 호출')
        qs = Board.objects.order_by('-id')
        page = request.GET.get('page', 1)
        # print('db_Board_List >> ', qs)
        board_list = qs.values()
        paginator = Paginator(board_list, 3)
        page_obj = paginator.get_page(page)

        context = {
            'list': page_obj
        }
        return render(request, 'board/boardList.html', context)
    else:
        return redirect('/sign/')


def insert(request):
    print('insert 호출')
    data = request.POST
    print('message >> ', data.get('message'))
    print('writer >> ', data.get('writer'))
    message = data.get('message')
    writer = data.get('writer')
    # writer = "YOO"

    try:
        # new_post = Board(content=data.get('message'), writer=data.get('writer'))
        new_post = Board(content=message, writer=writer)
        print(new_post)
        new_post.save()

        return redirect('/board')
    except:
        print("글쓰기 실패")
        return redirect('/board')
