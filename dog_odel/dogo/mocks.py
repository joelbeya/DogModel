from django.http import Http404

class Dog(object):
    """docstring for Dog."""
    Dog = [
        {'id':1, 'title':'Labrador retriever', 'body':'Nzoto bwa ya yambo'},
        {'id':2, 'title':'Golden Retriever', 'body':'Nzoto bwa ya mibale'},
        {'id':3, 'title':'Berger allemand', 'body':'Nzoto bwa ya misato'},
        {'id':4, 'title':'Dogue de Bordeaux, ', 'body':'Nzoto bwa ya minei'},
        {'id':5, 'title':'Levrier Ecossais', 'body':'Nzoto bwa ya sambo'},
        {'id':6, 'title':'Lévrier Hongrois', 'body':'Nzoto bwa ya sambo'},
        {'id':7, 'title':'Sloughi', 'body':'Nzoto bwa ya sambo'},
        {'id':8, 'title':'Terrier du Tibet', 'body':'Nzoto bwa ya sambo'},

    ]

    # def __init__(self, arg):
    #     super(Dog, self).__init__()
    #     self.arg = arg

    @classmethod
    def all(cls):
        return cls.Dog

    @classmethod
    def find(cls, id):
        try:
            return cls.Dog[int(id) - 1]
        except:
            raise Http404('Google who are you {} ?')
