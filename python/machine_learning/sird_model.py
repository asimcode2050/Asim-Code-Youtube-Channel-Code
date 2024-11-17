import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
beta = 0.3
gamma = 0.1
mu = 0.05
S0 = 990
I0 = 10
R0 = 0
D0 = 0
N = S0 + I0 + R0 + D0
t = np.linspace(0, 160, 160)


def SIRD_model(y, t, beta, gamma, mu):
    S, I, R, D = y
    if not isinstance(y, (list, np.ndarray)):
        raise ValueError(f"Expected a list or array for 'y', got {
                         type(y)} instead.")
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I - mu * \
        I  # infected individuals recover or die
    dRdt = gamma * I
    dDdt = mu * I
    return [dSdt, dIdt, dRdt, dDdt]


y0 = [S0, I0, R0, D0]
sol = odeint(SIRD_model, y0, t, args=(beta, gamma, mu))
S = sol[:, 0]
I = sol[:, 1]
R = sol[:, 2]
D = sol[:, 3]
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible', color='blue')
plt.plot(t, I, label='Infected', color='red')
plt.plot(t, R, label='Recovered', color='green')
plt.plot(t, D, label='Deceased', color='black')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('SIRD Model')
plt.legend()
plt.grid(True)
plt.show()
