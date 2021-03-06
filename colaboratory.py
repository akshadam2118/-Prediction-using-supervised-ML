# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:50:15 2022

@author: ak
"""

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled12.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPM3MgJc6Auhu0HlxRTPJbO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tejal562/Prediction-using-supervised-ML/blob/main/Untitled12.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tNUSYC1zHUwd"
      },
      "source": [
        "The Sparks Foundation - Data Science and Business Analytics Internship\r\n",
        "\r\n",
        "Name - Tejal jadhav\r\n",
        "\r\n",
        "TASK 1 - Prediction using Supervised ML\r\n",
        "\r\n",
        "To Predict the percentage of marks of the students based on the number of hours they studied"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aerXmBZBEzHF"
      },
      "source": [
        "# importing the required libraries\r\n",
        "import pandas as pd\r\n",
        "import numpy as np\r\n",
        "import matplotlib.pyplot as plt \r\n",
        "import seaborn as sns\r\n",
        "from sklearn.model_selection import train_test_split\r\n",
        "from sklearn.linear_model import LinearRegression\r\n",
        "from sklearn.metrics import mean_absolute_error"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "xD2zJqi4E-EO",
        "outputId": "c1be04f1-e5c5-4a7e-fe64-99374a512303"
      },
      "source": [
        "# Reading the Data \r\n",
        "data = pd.read_csv('http://bit.ly/w-data')\r\n",
        "data.head(5)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Hours</th>\n",
              "      <th>Scores</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2.5</td>\n",
              "      <td>21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>5.1</td>\n",
              "      <td>47</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3.2</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>8.5</td>\n",
              "      <td>75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>3.5</td>\n",
              "      <td>30</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Hours  Scores\n",
              "0    2.5      21\n",
              "1    5.1      47\n",
              "2    3.2      27\n",
              "3    8.5      75\n",
              "4    3.5      30"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AjoWXYROFOug",
        "outputId": "88ace36e-7a04-4d72-9db2-19f16493469e"
      },
      "source": [
        "# Check if there any null value in the Dataset\r\n",
        "data.isnull == True"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "OcX7fGuDFWYU",
        "outputId": "41712fdf-fb09-49c1-8b47-13ca0764983d"
      },
      "source": [
        "sns.set_style('darkgrid')\r\n",
        "sns.scatterplot(y= data['Scores'], x= data['Hours'])\r\n",
        "plt.title('Marks Vs Study Hours',size=20)\r\n",
        "plt.ylabel('Marks Percentage', size=12)\r\n",
        "plt.xlabel('Hours Studied', size=12)\r\n",
        "plt.show()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYEAAAEeCAYAAABsaamyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deVxU9f7H8dewKaKAGoug95YUSpS4bykpJKCooIamhooZeq+K+1Ka3uvtmrey7GZdIy3RbBFCNDU3yLBw19LM0jTNDVAUURGBmfn9gcxPYjsos3+ejwePh5w5M+c94zCf+Z7v93y/Kq1Wq0UIIYRVsjF2ACGEEMYjRUAIIayYFAEhhLBiUgSEEMKKSREQQggrJkVACCGsmBQBUWMtWrQgOjra2DEEMHv2bFq0aMH58+eNHUWYKSkCJqxFixa0aNGCli1b8scff1S6X3R0tG7f5ORkAybUr99//50WLVrQvXt31Gp1lfseOnSIFi1a0L9//1rNcOfOHVasWEFUVBTt2rXjiSeeoFu3bgwcOJAFCxawb9++Mvu/++67tGjRgr1799ZqDmMpfW9V9XxKC5ElvfesiRQBE2dnZ4dWqyUpKanC28+cOcO+ffuws7MzcDL9e+SRR+jYsSPZ2dns3Lmzyn0TExMBGDJkSK0d/9atWwwdOpTXX3+dS5cuERISwujRowkLC6NevXqsXbuWtWvX1trxhDAGy/vksDCNGzfGzc2N5ORk4uLiyn3Yl3749ezZk+3btxsjol4NHjyYffv2kZiYSHBwcIX73Lx5ky1btuDo6FirLYGEhASOHTtGt27d+N///oeDg0OZ269fv86pU6dq7XhCGIO0BMzA4MGDuXz5crlvw0VFRaxbt442bdrg4+NT4X1/+uknXn31Vfr370/Hjh158sknCQkJYdGiRVy/fr3c/snJybqmfXp6OtHR0bRr144WLVpUm3P58uW0bNmS5557jtzcXAAKCwtZtWoVAwYMoEOHDgQEBBAUFMTf/vY3MjIyqn3M0NBQXF1dSU9PJysrq8J9vvrqK/Lz8+nduzcNGjTQbT9w4ADjxo0jMDCQJ554gqeeeorBgwezdOnSao8LcPjwYQCGDh1argAAuLi40LZtW93vQUFBusceMWKE7hTdva9d6emVitz72v9ZRkYGw4YNo3Xr1nTs2JG///3vFRagU6dOVdtn069fP/z9/cnOzq50n9py5swZZs6cSffu3XWn0mbOnMmZM2fK7VtV/8bevXtp0aIF7777bpntpa9nYWEhS5cuJTQ0lCeeeILZs2cDD/7+swbSEjAD4eHhLFq0iMTERJ555hnd9rS0NHJycpg+fTpnz56t8L5r165lx44ddOjQga5du6LRaDh27Bgff/wx6enprF27lvr165e739atW9m1axeBgYE899xzXLx4sdJ8Go2GhQsXsnr1akJCQnjzzTepU6cOAC+99BIbN27E19eXiIgI6tatS3Z2NgcPHmTXrl107dq1yufu4OBAREQECQkJJCcn87e//a3cPqWtoaioKN229PR0xo4dS/369QkKCsLDw4Pc3FxOnz7Np59+yoQJE6o8LoCrqytQ0jehxIgRI0hNTWXfvn0MGDAAb29vRferzpYtW5gyZQr29vb06dMHNzc3Dh48yHPPPVeuoPj4+NCpUyf27t3L77//ziOPPFLm9kOHDnHixAlCQ0Nxd3evlXyVOXLkCDExMdy6dYugoCAeffRRTp8+zYYNG0hNTeXjjz+mVatWtXKsuLg4jh49SmBgIM888wyNGzcGHvz9Zw2kCJiB+vXr06dPH9atW0dmZiaenp4Aug/w3r17s2zZsgrvO3bsWObPn4+trW2Z7YmJicydO5dPP/2U2NjYcvf79ttviY+PJzAwsMpsd+7cYfr06Wzbto3nn3+eOXPmYGNT0sC8ceMGmzZtwt/fn8TExHIZrl27puj5DxkyhISEBJKSkhg3bhwqlUp32/Hjxzl27Bi+vr5lvpUnJiai0WhYvXo1LVu2LPN4V69eVXTcPn36sGHDBt555x0uXLhAjx49ePzxxyv98Bw1ahQ3btzQFYFOnTopOk5Vbt26xfz587GxsWHNmjU8+eSTutsWLlxIQkJCufsMGzaMvXv3snbtWmbNmlXmttI+jJr2naxbt65cJ3ip48ePl9um1WqZNWsWN2/e5I033ihzmm7z5s1MmTKFmTNnsnnzZt375UFcuHCBr776ikaNGum21db7z9LJ6SAzMXjwYNRqta6D+MKFC2RkZNCvXz8cHR0rvZ+3t3e5Nz/As88+S/369fnuu+8qvF9wcHC1BSA3N5dRo0axfft2pk+fziuvvFLmD1qlUqHVanFwcKjwD71hw4ZVPn4pHx8f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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 354
        },
        "id": "rQS9DRXJFiUA",
        "outputId": "a47321a9-a9e2-4e3e-e73e-e11cc5019d88"
      },
      "source": [
        "sns.regplot(x= data['Hours'], y= data['Scores'])\r\n",
        "plt.title('Regression Plot',size=20)\r\n",
        "plt.ylabel('Marks Percentage', size=12)\r\n",
        "plt.xlabel('Hours Studied', size=12)\r\n",
        "plt.show()\r\n",
        "print(data.corr())"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEeCAYAAACQfIJ4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeXxTdbr48c/J1qRLWgrdC8hiy1Ipq4oOqKjgiAooKIIM6jh4r3dwGa8L41VnU+/P1yzccb2OOoqKGwIyjtcNRFCUpewCMsoi3aG0TZekWc75/ZEmbdq0TZe0aXner9e8Sk9PkqfN2KfnfL/P8yiapmkIIYQQTeh6OgAhhBCRSRKEEEKIoCRBCCGECEoShBBCiKAkQQghhAhKEoQQQoigJEEI0QOys7NZtGhRT4fRYfn5+WRnZ/Pggw/2dCgijAw9HYDovbKzswM+1+l0xMXFkZ2dzZw5c5gzZw6KovRQdKK9gr2fVquV7Oxs5s2bx9VXX93lr7l69WqWLVvGE088wbXXXtvlzy86RxKE6LRf/vKXALjdbo4fP85nn33Gtm3b2L9/P4888kgPRxeZPvzwQywWS0+HEVTj9/PIkSOsX7+erVu3sn//fpYtW9bD0YnuJAlCdNrSpUsDPs/Ly+Omm25i5cqV3HLLLQwcOLCHIotcw4YN6+kQWtT0/fz666+55ZZbePXVV1m0aBGZmZk9FJnobrIGIbrchAkTGDp0KJqm8e233zb7+p49e7jzzju58MILycnJ4aKLLuKRRx6hpKQk6PPt3buXW2+9lXHjxjF+/Hhuvvlmdu3axVNPPUV2djZbt24NON93f//kyZM89NBDTJkyhZEjR7J69eoOxXDixAkefvhhLr/8csaMGcO5557L1VdfzSOPPEJ5ebn/PKfTyYoVK5gzZw6TJk0iNzeXadOm8e///u9s2bIlaIxNVVVV8ac//YkZM2ZwzjnnMGnSJH7+8583ezzA1q1byc7O5qmnnuLgwYMsWbKEiRMnkpuby0033cTOnTuD/jzba/Lkyf73c9++fW2eX1paym9/+1umTZtGTk4O559/Pr/85S/Zv39/wHmLFi3yX5EsW7aM7Oxs///y8/O7JHbROXIFIcLKYAj8v9iqVat45JFHMJlMTJs2jdTUVI4fP867777Lhg0beOedd0hPT/efv337dm699VZUVeXyyy9n0KBBHD58mJ/97Gecf/75Lb5uRUUFN9xwA9HR0UyfPh1FUejfv3+7YygtLWXu3LlUV1czdepUpk+fTl1dHfn5+axbt46bbrqJfv36Ad5fch988AFZWVnMmjULs9lMaWkpeXl5bN68mQsuuKDVn5XNZuPGG2/k+++/55xzzmHx4sWUl5fzf//3f9x666385je/Yf78+c0et3//fl588UXGjh3LvHnzKCws5JNPPuHmm29m7dq1DB06NLQ3qxW+lm1trSmdOHGCBQsWUFpayvnnn8/MmTMpKirio48+YuPGjTz11FNccsklAMyZM4e4uDjWr1/PpZdeysiRI/3PY7VaOx2z6AKaEB2UlZWlZWVlNTu+bds2bcSIEdro0aO1kpIS//EjR45oo0eP1i677DKtuLg44DFbtmzRRowYod1xxx3+Yx6PR7v88su1rKwsbePGjQHnr1y50v/633zzTdC47rvvPs3lcgV8rb0xrFixQsvKytJeeeWVZt9nTU2NZrfbNU3TNJvNpmVnZ2tz5szR3G53s3NPnz7dLMabbrop4NjDDz+sZWVlaQ8//LCmqqr/+NGjR7Xx48dro0eP1k6cOOE//s033/i/1/feey/gud58800tKytLe/TRR5vF0pKW3s+vvvpKy87O1rKzs7X8/HxN0zTtxIkTWlZWlvbAAw8EnHvrrbdqWVlZ2rPPPhtwPC8vTxs5cqR27rnnatXV1f7j7733XtD4RWSQKwjRaU899RQQuEitaRoPPPAAycnJ/vPefPNNXC4XDz30ECkpKQHPMXnyZKZNm8bnn39OdXU1sbGx7Ny5k+PHj3Peeedx0UUXBZx/ww038Morr3Ds2LGgMRmNRh544IFmVzDtjcHHbDY3e43o6Gj/vxVFQdM0TCYTOl3zO7e+q4yWOJ1O1q1bR3R0NL/61a8C/lI/66yzWLRoEc899xxr1671LyL7jB8/vtkOoOuuu47f//737N27t9XXDabx+3n06FH/+3nzzTeTkZHR4uOKi4v58ssvSU9P57bbbmsW48yZM1m3bh2ffvops2fPbndcovtJghCd9vTTTwd8rigKjz32GNddd13A8d27dwOwbdu2oPeyy8rK8Hg8HDt2jJycHA4ePAh41zSa0ul0jB8/vsUEkZGR4b+l1JkYpk2bxp///Gd+97vf8eWXX/KTn/yE8ePHM3z48IBf4rGxsVxyySV8/vnnzJo1i+nTp/vXA0LZrXT06FHsdjvjx48nISGh2dfPP/98nnvuOf/PpLGcnJxmx4xGI/3798dms7X52k353k9FUbBarUyYMIG5c+cya9asVh934MABwPt+GY3GoN/DunXrOHDggCSIXkIShOi07777DoDa2lp2797NQw89xKOPPkp6ejqTJ0/2n1dRUQHASy+91Orz1dbWAt4FW4ABAwYEPS9YAvBJSkoKery9MWRkZLBq1SqeeuopNm/ezCeffAJAWloat956Kz/72c/8j1m+fDl/+9vf+OCDD/x/hUdFRTFjxgweeOCBFr8PaPheW4rbdzzYL/yW7tcbDAZUVW31+wzG9362V6jfg+88EfkkQYguEx0dzQUXXMBzzz3Htddey4MPPshHH33k/wvad8smLy8v4PZNS3znnDp1KujXy8rKWnxsS4up7Y0BvFtSly9fjtvt5tChQ2zZsoXXX3+dxx57DIvFwrx58wDvbailS5eydOlSioqK2L59O2vWrGHdunUUFBSwcuXKFl8jLi6u1e/15MmTAedFolC/h1B/7qLnyTZX0eVGjBjBvHnzKC4u5pVXXvEfHzt2LAA7duwI6XlGjRoFeH+ZN6Wqaoe2cbY3hsYMBgM5OTksWbKEP//5zwCsX78+6LlpaWlcc801vPTSSwwePJi8vLyALbFNDRkyBIvFwqFDh4JeJfi28vp+JpGo8fvldrubfd33PYwePdp/zLde4/F4uiFC0V6SIERY3HHHHZhMJl5++WUqKysBWLhwIUajkSeeeIKjR482e4zT6Qz4xT1+/HgGDRrE1q1b+eKLLwLOffvtt1tcf2hNe2PYv39/0Fsivr+SfYvXp0+fDnprpra2ltraWgwGQ9D78j4mk4mrr76ampoa/ud//ifgaz/++COvvfYaRqOxzXWAnpSamsqFF15IQUEBr776asDX9uzZwwcffEB8fDyXXXaZ/7hv8b6oqKhbYxWhkVtMIixSUlKYP38+K1as4MUXX+Tee+9l2LBhPPbYYzz00ENcddVVTJkyhbPOOgu3201hYSF5eXn069ePjz76CPD+dfmHP/yB2267jTvuuIPp06czaNAgvvvuO7766iumTp3Kpk2bgu4aakl7Y3j//fd5++23mTBhAgMHDiQ+Pp4ff/yRzz//HJPJ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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "           Hours    Scores\n",
            "Hours   1.000000  0.976191\n",
            "Scores  0.976191  1.000000\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Px6p0tp3IYKE"
      },
      "source": [
        "It is confirmed that the variables are positively correlated.\r\n",
        "\r\n",
        "Training the Model\r\n",
        "\r\n",
        "1) Splitting the Data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aPvjD7-xFklF"
      },
      "source": [
        "# Defining X and y from the Data\r\n",
        "X = data.iloc[:, :-1].values  \r\n",
        "y = data.iloc[:, 1].values\r\n",
        "\r\n",
        "# Spliting the Data in two\r\n",
        "train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x8VMuZqZF3Et",
        "outputId": "4e57d45f-e6bf-4020-ae47-12e68158d92a"
      },
      "source": [
        "regression = LinearRegression()\r\n",
        "regression.fit(train_X, train_y)\r\n",
        "print(\"---------Model Trained---------\")"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---------Model Trained---------\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yRVhMy8SJN6p"
      },
      "source": [
        "Predicting the Percentage of Marks"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 254
        },
        "id": "U8p0griVF7sW",
        "outputId": "6d3e4e9e-c2a3-429d-f60e-80771e887b4a"
      },
      "source": [
        "pred_y = regression.predict(val_X)\r\n",
        "prediction = pd.DataFrame({'Hours': [i[0] for i in val_X], 'Predicted Marks': [k for k in pred_y]})\r\n",
        "prediction"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Hours</th>\n",
              "      <th>Predicted Marks</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.5</td>\n",
              "      <td>16.844722</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>3.2</td>\n",
              "      <td>33.745575</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.4</td>\n",
              "      <td>75.500624</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2.5</td>\n",
              "      <td>26.786400</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.9</td>\n",
              "      <td>60.588106</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>3.8</td>\n",
              "      <td>39.710582</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>1.9</td>\n",
              "      <td>20.821393</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Hours  Predicted Marks\n",
              "0    1.5        16.844722\n",
              "1    3.2        33.745575\n",
              "2    7.4        75.500624\n",
              "3    2.5        26.786400\n",
              "4    5.9        60.588106\n",
              "5    3.8        39.710582\n",
              "6    1.9        20.821393"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S665OplHJUHa"
      },
      "source": [
        "Comparing the Predicted Marks with the Actual Marks"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 254
        },
        "id": "aQcBiNRlF-FQ",
        "outputId": "ba243da7-0fd1-4c68-af43-65caac526bf3"
      },
      "source": [
        "compare_scores = pd.DataFrame({'Actual Marks': val_y, 'Predicted Marks': pred_y})\r\n",
        "compare_scores"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Actual Marks</th>\n",
              "      <th>Predicted Marks</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>20</td>\n",
              "      <td>16.844722</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>27</td>\n",
              "      <td>33.745575</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>69</td>\n",
              "      <td>75.500624</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>30</td>\n",
              "      <td>26.786400</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>62</td>\n",
              "      <td>60.588106</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>35</td>\n",
              "      <td>39.710582</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>24</td>\n",
              "      <td>20.821393</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Actual Marks  Predicted Marks\n",
              "0            20        16.844722\n",
              "1            27        33.745575\n",
              "2            69        75.500624\n",
              "3            30        26.786400\n",
              "4            62        60.588106\n",
              "5            35        39.710582\n",
              "6            24        20.821393"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dJG3g6IWJf9q"
      },
      "source": [
        "Visually Comparing the Predicted Marks with the Actual Marks"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "V3sueDCVGP73",
        "outputId": "b139e2cf-69b3-4198-814c-67d8c290f377"
      },
      "source": [
        "plt.scatter(x=val_X, y=val_y, color='blue')\r\n",
        "plt.plot(val_X, pred_y, color='Black')\r\n",
        "plt.title('Actual vs Predicted', size=20)\r\n",
        "plt.ylabel('Marks Percentage', size=12)\r\n",
        "plt.xlabel('Hours Studied', size=12)\r\n",
        "plt.show()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YdKk9P_XGWGT",
        "outputId": "a672edeb-8722-4169-f30b-d829de3aeabb"
      },
      "source": [
        "# Calculating the accuracy of the model\r\n",
        "print('Mean absolute error: ',mean_absolute_error(val_y,pred_y))"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mean absolute error:  4.130879918502482\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rNMH-V5pLrsh"
      },
      "source": [
        "What will be the predicted score of a student if he/she studies for 9.25 hrs/ day?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eHdcm-U8GqEf",
        "outputId": "d0ea2cc9-b4ff-4434-ee26-4c1008ec13fb"
      },
      "source": [
        "hours = [9.25]\r\n",
        "answer = regression.predict([hours])\r\n",
        "print(\"Score = {}\".format(round(answer[0],3)))"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Score = 93.893\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
} 