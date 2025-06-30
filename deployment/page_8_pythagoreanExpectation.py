import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import streamlit as st

@st.cache_data
def preparing_data():
    data = pd.read_csv(r"database/games.csv")

    data = data[['home', 'away', 'h_pts', 'a_pts', 'date']]
    data = data.rename(columns={'home': 'h_team', 'away': 'a_team'})

    data['h_win'] = 0
    for i in range(len(data['h_pts'])):
        if data['h_pts'].iloc[i] > data['a_pts'].iloc[i]:
            data.iloc[i, 5] = 1

    data['a_win'] = np.where(data['h_pts'] < data['a_pts'], 1, 0)

    data['count'] = 1

    # performance of teams at home
    home = data.groupby('h_team')[['h_win', 'h_pts', 'a_pts', 'count']].sum().reset_index()
    home = home.rename(columns={'h_team': 'team', 'h_pts': 'pts_h', 'a_pts': 'opp_pts_h', 'count': 'h_games'})


    # performance of teams on the road
    away = data.groupby('a_team')[['a_win', 'h_pts', 'a_pts', 'count']].sum().reset_index()
    away = away.rename(columns={'a_team': 'team', 'h_pts': 'opp_pts_a', 'a_pts': 'pts_a', 'count': 'a_games'})

    # merging for each team
    df = pd.merge(home, away, on='team')

    return df


def pythagoreanExp_calculation(data):
    data['wins'] = data['h_win'] + data['a_win']
    data['games_played'] = data['h_games'] + data['a_games']
    data['pts_scored'] = data['pts_h'] + data['pts_a']
    data['pts_opp'] = data['opp_pts_h'] + data['opp_pts_a']

    # defining win% and pythagorean expectation
    data['win%'] = data['wins'] / data['games_played']
    data['p_expectation'] = data['pts_scored'] ** 2 / (data['pts_scored'] ** 2 + data['pts_opp'] ** 2)

    return data


if __name__ == '__main__':
    # Heading
    st.title('Pythagorean expectation of teams in 2022/23')

    # preparing the data
    df = preparing_data()

    #calculating win% and pyth expec...
    df=pythagoreanExp_calculation(df)

    st.markdown("The expected performance of a team over a season is given by the formula:")
    st.latex(r"""
    \frac{\left(\text{pts scored}\right)^2}
    {\left(\text{pts scored}\right)^2 + \left(\text{opponents pts}\right)^2}
    """)

    st.markdown("This should be approximately equal to the win% of the team for the entire season.")

    #plotting my linear correlation plot
    st.markdown("")
    st.pyplot(sns.relplot(x='p_expectation', y='win%', data=df))

    #creating a regression analysis
    df.rename(columns={'win%': 'win_percent'}, inplace=True)
    pyth_lm = smf.ols(formula='win_percent~p_expectation', data=df).fit()
    st.markdown("")
    st.subheader("Regression results")
    st.write(pyth_lm.summary())

    #my analysis
    st.markdown("")
    st.markdown("""
    The regression output tells you many things about the fitted relationship between win percentage and the Pythagorean Expectation. Regression is a method for identifying an equation which best fits the data. In this case that relationship is:
	
	        win% = (Intercept + coef) * p_expectation
	""")

    st.markdown("""
(i) I observed an R-squared of 0.913, indicating a strong relationship between both variables. This means 91.3% of the variance in win_percent is explained by p_expectation
	
(ii) You can see the value of Intercept is -2.8414 and coef is 6.6794. It's this latter value were interested in (Because having a p_expectation of 0 will be crazy!). It means that for every 1 unit increase in p_expectation, the win percentage increases by 6.68 percentage points (on average).

(iii) The standard error (std err) gives us an idea of the precision of the estimate: 0.389 is solid.
	 
    The ratio of the coefficient (coef) to the standard error is called the t statistic (t) and its value informs us about statistical significance. This is illustrated by the p-value (P > |t|) - this is the probability that we would observe the value 6.6794 by chance, if the true value were really zero. This probability here is 0.000 - (this is not exactly zero, but the table doesn't include enough decimal places to show this) which means we can confident it is not zero. By convention, it is usual to conclude that we cannot be confident that the value of the coefficient is not zero if the p-value is greater than .05

    """)

    st.subheader("Notes:")
    st.markdown("• My basketball data is not completely cleaned as it contains playoffs and play-in tournament games")


