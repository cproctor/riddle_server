from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from app.models import Riddle

@route_get('all', args={})
def list_riddles(params):
    riddles = sorted(Riddle.objects.all(), key=lambda riddle: riddle.difficulty())
    return {'riddles': [riddle.to_dict(with_answer=False) for riddle in riddles]}

@route_post('new', args={'question': str, 'answer': str})
def create_riddle(params):
    riddle = Riddle.from_dict(params)
    errors = riddle.validate()
    if len(errors) == 0:
        riddle.save()
        return riddle.to_dict(with_answer=False)
    else:
        raise BadRequest()
        
@route_get('show', args={'id': int})
def show_riddle(params):
    try:
        riddle = Riddle.objects.get(id=params['id'])
        return riddle.to_dict(with_answer=False)
    except Riddle.DoesNotExist:
        raise BadRequest()

@route_post('guess', args={'id': int, "answer": str})
def guess_answer(params):
    try:
        riddle = Riddle.objects.get(id=params['id'])
        correct = riddle.check_guess(params['answer'])
        return {
            "guess": params['answer'], 
            "correct": correct,
            "riddle": riddle.to_dict(with_answer=correct)
        }
    except Riddle.DoesNotExist:
        raise BadRequest()
    
