import framework
from agent_tabular_ql import run_episode


def visualize_path():
    _, history = run_episode(for_training=False, need_history=True)
    print('Quest : ', history[0][1])
    for el in history:
        print('Current : {}, action taken : {} {}, next : {}, reward : {}, done : {}'.format(
            el[0], framework.actions[el[2]], framework.objects[el[3]], el[4], el[6], el[7]))

visualize_path()
