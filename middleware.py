from urllib import response


class samplemiddleware:
    def __init__(self,getresponse):
        self.getresponse=getresponse
    
    def __call__(self,request):
        response=self.getresponse(request)
        print('sample middleware')
        print(request.COOKIES)
        return response