from pyhop_anytime import *


def go(state, entity, start, end):
    if state.loc[entity] == start and end in state.connected[start] and end not in state.visited[entity]:
        state.loc[entity] = end
        state.visited[entity].append(end)
        return state


def find_route(state, entity, start, end):
    if start == end:
        return TaskList(completed=True)
    elif end in state.connected[start]:
        return TaskList([('go', entity, start, end)])
    else:
        return TaskList([[('go', entity, start, neighbor), ('find_route', entity, neighbor, end)]
                         for neighbor in state.connected[start]])


def make_travel_planner():
    planner = Planner()
    planner.declare_operators(go)
    planner.declare_methods('find_route', find_route)
    return planner


def setup_state(title, people, connections):
    state = State(title)
    state.visited = {person: [] for (person, location) in people}
    state.loc = {person: location for (person, location) in people}
    state.connected = {}
    for (loc1, loc2) in connections:
        if loc1 not in state.connected:
            state.connected[loc1] = []
        if loc2 not in state.connected:
            state.connected[loc2] = []
        state.connected[loc1].append(loc2)
        state.connected[loc2].append(loc1)
    return state


state = setup_state('state',
                    [('robot', 'mcrey312')],
                    [('mcrey312', 'hallway'), ('mcrey312', 'mcrey314'), ('mcrey314', 'hallway'), ('lounge', 'hallway'),
                     ('copyroom', 'lounge')])
planner = make_travel_planner()
plans = planner.anyhop(state, [('find_route', 'robot', 'mcrey312', 'copyroom')])
for plan, time in plans:
    print(time)
    print(plan)