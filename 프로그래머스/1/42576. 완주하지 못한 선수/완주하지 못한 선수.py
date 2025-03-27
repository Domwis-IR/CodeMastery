def solution(participant, completion):
    completion_player = {}
    for complete_player in completion:
        completion_player[complete_player] = completion_player.get(complete_player, 0) + 1
    
    for runner in participant:
        if completion_player.get(runner, 0) == 0:
            return runner
        else:
            completion_player[runner] -= 1