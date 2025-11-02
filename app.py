{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMasBzu7yfZ0j22h8REtu+B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/apostle24/Business-profit--App/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hehBc9yXw_jp",
        "outputId": "23cca156-6907-461c-b261-09b41d033401"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.51.0)\n",
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.12/dist-packages (7.4.1)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.12/dist-packages (1.6.1)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.0)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow<22,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.12/dist-packages (from pyngrok) (6.0.3)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.16.3)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.5.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (3.6.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.10.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.10.5)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.28.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pyngrok scikit-learn pandas"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "# =======================\n",
        "# BUSINESS PREDICTION APP\n",
        "# By NB Joshua\n",
        "# =======================\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_absolute_error, mean_squared_error\n",
        "import streamlit_authenticator as stauth\n",
        "\n",
        "# ---- PAGE SETTINGS ----\n",
        "st.set_page_config(\n",
        "    page_title=\"Business Profile Prediction App\",\n",
        "    page_icon=\"💼\",\n",
        "    layout=\"wide\",\n",
        "    initial_sidebar_state=\"expanded\"\n",
        ")\n",
        "\n",
        "# ---- SIDEBAR ----\n",
        "with st.sidebar:\n",
        "    st.image(\"https://faithconncthub.store/wp-content/uploads/2024/12/logo.png\", caption=\"FaithConnct Hub\")\n",
        "    st.title(\"💼 Business Prediction App\")\n",
        "    st.markdown(\"Predict your business success potential instantly.\")\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"🌐 Connect With Me\")\n",
        "    st.write(\"Instagram: [@nbjoshua6](https://instagram.com/nbjoshua6)\")\n",
        "    st.write(\"🌍 [Website](https://faithconncthub.store)\")\n",
        "    st.write(\"📩 nbjoshua8@gmail.com\")\n",
        "    st.write(\"📞 +233 556 231 984\")\n",
        "    st.write(\"❤️ [Support or Donate](https://selar.com/showlove/nbjoshua)\")\n",
        "    st.markdown(\"---\")\n",
        "    st.caption(\"© 2025 NB Joshua | All Rights Reserved\")\n",
        "\n",
        "# ---- LOGIN SYSTEM ----\n",
        "names = [\"NB Joshua\", \"Premium User\"]\n",
        "usernames_list = [\"admin\", \"premium\"]\n",
        "passwords = [\"12345\", \"PREMIUM2025\"]\n",
        "\n",
        "# Create the credentials dictionary as expected by streamlit_authenticator\n",
        "credentials = {\n",
        "    \"usernames\": {\n",
        "        usernames_list[i]: {\"name\": names[i], \"password\": passwords[i]}\n",
        "        for i in range(len(usernames_list))\n",
        "    }\n",
        "}\n",
        "\n",
        "authenticator = stauth.Authenticate(credentials, \"business_app\", \"abcdef\", 30)\n",
        "name, auth_status, username = authenticator.login(\"Login\", \"main\")\n",
        "\n",
        "if auth_status:\n",
        "    authenticator.logout(\"Logout\", \"sidebar\")\n",
        "    st.sidebar.success(f\"✅ Logged in as: {name}\")\n",
        "\n",
        "    # --- Main Application Content ---\n",
        "    st.title(\"🚀 Business Profile Prediction\")\n",
        "    st.write(\"Fill in the details below to predict your business success.\")\n",
        "\n",
        "    # --- Sample data upload or use built-in data ---\n",
        "    uploaded_file = st.file_uploader(\"Upload a CSV file with R&D Spend, Administration, Marketing Spend, Profit\", type=[\"csv\"])\n",
        "\n",
        "    if uploaded_file:\n",
        "        data = pd.read_csv(uploaded_file)\n",
        "    else:\n",
        "        # Example data\n",
        "        data = pd.DataFrame({\n",
        "            \"R&D Spend\": [165349.20, 162597.70, 153441.51, 144372.41, 142107.34],\n",
        "            \"Administration\": [136897.80, 151377.59, 101145.55, 118671.85, 91391.77],\n",
        "            \"Marketing Spend\": [471784.10, 443898.53, 407934.54, 383199.62, 366168.42],\n",
        "            \"Profit\": [192261.83, 191792.06, 191050.39, 182901.99, 166187.94]\n",
        "        })\n",
        "\n",
        "    st.subheader(\"📊 Data Preview\")\n",
        "    st.write(data.head())\n",
        "\n",
        "    # --- ML model ---\n",
        "    X = data[[\"R&D Spend\", \"Administration\", \"Marketing Spend\"]]\n",
        "    y = data[\"Profit\"]\n",
        "\n",
        "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "    model = LinearRegression()\n",
        "    model.fit(X_train, y_train)\n",
        "\n",
        "    # --- User Input ---\n",
        "    st.header(\"Input New Business Data\")\n",
        "    rd = st.number_input(\"R&D Spend\", 0.0, 1000000.0, 100000.0)\n",
        "    admin = st.number_input(\"Administration\", 0.0, 1000000.0, 50000.0)\n",
        "    market = st.number_input(\"Marketing Spend\", 0.0, 1000000.0, 200000.0)\n",
        "\n",
        "    # --- Prediction ---\n",
        "    input_data = pd.DataFrame({\"R&D Spend\": [rd], \"Administration\": [admin], \"Marketing Spend\": [market]})\n",
        "    prediction = model.predict(input_data)[0]\n",
        "\n",
        "    st.subheader(\"💰 Predicted Profit:\")\n",
        "    st.write(f\"${prediction:,.2f}\")\n",
        "\n",
        "    # --- Model performance ---\n",
        "    y_pred = model.predict(X_test)\n",
        "    st.write(f\"MAE: {mean_absolute_error(y_test, y_pred):.2f}\")\n",
        "    st.write(f\"MSE: {mean_squared_error(y_test, y_pred):.2f}\")\n",
        "\n",
        "    # --- Payment & Contact Section ---\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"💳 Upgrade to ProfitSense Pro\")\n",
        "\n",
        "    st.write(\"\"\"\n",
        "    Get advanced business insights, unlimited predictions, and detailed profit reports.\n",
        "    Support the creator and unlock all premium features.\n",
        "    \"\"\")\n",
        "\n",
        "    # Payment link (Selar)\n",
        "    st.markdown(\"[👉 Click here to upgrade or show love](https://selar.com/showlove/nbjoshua)\")\n",
        "\n",
        "    st.write(\"**Payments powered by Selar**\")\n",
        "\n",
        "    # Contact Info\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"📞 Contact Joshua\")\n",
        "\n",
        "    st.write(\"\"\"\n",
        "    Need a custom business analysis or an AI app like this?\n",
        "    Let's connect 👇\n",
        "\n",
        "    - 📧 **Email:** [nbjoshua8@gmail.com](mailto:nbjoshua8@gmail.com)\n",
        "    - 🌐 **Website:** [faithconncthub.store](https://faithconncthub.store)\n",
        "    - 📱 **Phone / WhatsApp:** +233 55 623 1984\n",
        "    - 📸 **Instagram:** [@nbjoshua6](https://instagram.com/nbjoshua6)\n",
        "    \"\"\")\n",
        "\n",
        "    # Optional: Promote your other links\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"💼 Explore More From Joshua\")\n",
        "    st.markdown(\"[🧠 Learn How to Build AI & Online Business](https://faithconncthub.store)\")\n",
        "    st.markdown(\"[❤️ Support on Selar](https://selar.com/showlove/nbjoshua)\")\n",
        "\n",
        "else:\n",
        "    if auth_status is False:\n",
        "        st.error(\"❌ Incorrect username or password.\")\n",
        "    elif auth_status is None:\n",
        "        st.warning(\"🔐 Please login to access the app.\")\n",
        "\n",
        "# ---- FOOTER ----\n",
        "st.markdown(\"---\")\n",
        "st.caption(\"Built with ❤️ by NB Joshua | Powered by Streamlit | [FaithConnctHub.store](https://faithconncthub.store)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hyf4DsL5x8gA",
        "outputId": "d2a3ec77-63ec-459b-b3b2-7d8c99feaf47"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "# IMPORTANT: Replace 'YOUR_AUTHTOKEN' with your actual ngrok authtoken.\n",
        "# You can get your authtoken from your ngrok dashboard: https://dashboard.ngrok.com/get-started/your-authtoken\n",
        "ngrok.set_auth_token(\"34pvq7x57YsTENSWIVmgQ7jlWC1_6HYm5C6LevBwSL2aSQrBT\")\n",
        "\n",
        "!streamlit run app.py &>/dev/null&\n",
        "public_url = ngrok.connect(8501)\n",
        "public_url"
      ],
      "metadata": {
        "id": "276P0twEyOas",
        "outputId": "9d465640-e04b-4a71-e208-651cde332b4f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": []
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<NgrokTunnel: \"https://undecayable-overcleanly-rhoda.ngrok-free.dev\" -> \"http://localhost:8501\">"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "!streamlit run app.py &>/dev/null&\n",
        "public_url = ngrok.connect(8501)\n",
        "public_url"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UKLi3EwZ1UBj",
        "outputId": "bacfbca5-a5fc-44d9-d625-9807fc1f7da6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<NgrokTunnel: \"https://undecayable-overcleanly-rhoda.ngrok-free.dev\" -> \"http://localhost:8501\">"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile requirements.txt\n",
        "streamlit\n",
        "scikit-learn\n",
        "pandas\n",
        "pyngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kGA7_Awy3rAH",
        "outputId": "766136d8-9a4d-42e1-a4c0-63f245dc61e2"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing requirements.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.download('app.py')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "GRuV4Zbq4vEw",
        "outputId": "8db46f49-ba27-48ba-c395-9aad48451411"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_f7dd6a1e-62a4-46b4-a770-e9d8efce77ab\", \"app.py\", 3202)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.download('requirements.txt')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "jud-fAzh45kJ",
        "outputId": "0f3902d7-7630-4775-c763-0f4fd59cca68"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_14539df7-89a7-427d-9eb9-ad14b49391a7\", \"requirements.txt\", 38)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "# --- Payment & Contact Section ---\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"💳 Upgrade to ProfitSense Pro\")\n",
        "\n",
        "st.write(\"\"\"\n",
        "Get advanced business insights, unlimited predictions, and detailed profit reports.\n",
        "Support the creator and unlock all premium features.\n",
        "\"\"\")\n",
        "\n",
        "# Payment link (Selar)\n",
        "st.markdown(\"[👉 Click here to upgrade or show love](https://selar.com/showlove/nbjoshua)\")\n",
        "\n",
        "st.write(\"**Payments powered by Selar**\")\n",
        "\n",
        "# Contact Info\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"📞 Contact Joshua\")\n",
        "\n",
        "st.write(\"\"\"\n",
        "Need a custom business analysis or an AI app like this?\n",
        "Let's connect 👇\n",
        "\n",
        "- 📧 **Email:** [nbjoshua8@gmail.com](mailto:nbjoshua8@gmail.com)\n",
        "- 🌐 **Website:** [faithconncthub.store](https://faithconncthub.store)\n",
        "- 📱 **Phone / WhatsApp:** +233 55 623 1984\n",
        "- 📸 **Instagram:** [@nbjoshua6](https://instagram.com/nbjoshua6)\n",
        "\"\"\")\n",
        "\n",
        "# Optional: Promote your other links\n",
        "st.markdown(\"---\")\n",
        "st.subheader(\"💼 Explore More From Joshua\")\n",
        "st.markdown(\"[🧠 Learn How to Build AI & Online Business](https://faithconncthub.store)\")\n",
        "st.markdown(\"[❤️ Support on Selar](https://selar.com/showlove/nbjoshua)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qOXQr_81Cify",
        "outputId": "ebea1aab-6827-48b0-9f7b-9d5a6832e9c4"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-11-02 03:52:52.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.461 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.463 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.465 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.468 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.473 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.476 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.476 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.481 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.482 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.489 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.502 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.508 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.513 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.526 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.530 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.531 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.535 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.538 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 03:52:52.545 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# =======================\n",
        "# BUSINESS PREDICTION APP\n",
        "# By NB Joshua\n",
        "# =======================\n",
        "\n",
        "import streamlit as st\n",
        "import streamlit_authenticator as stauth\n",
        "\n",
        "# ---- PAGE SETTINGS ----\n",
        "st.set_page_config(\n",
        "    page_title=\"Business Profile Prediction App\",\n",
        "    page_icon=\"💼\",\n",
        "    layout=\"wide\",\n",
        "    initial_sidebar_state=\"expanded\"\n",
        ")\n",
        "\n",
        "# ---- SIDEBAR ----\n",
        "with st.sidebar:\n",
        "    st.image(\"https://faithconncthub.store/wp-content/uploads/2024/12/logo.png\", caption=\"FaithConnct Hub\")\n",
        "    st.title(\"💼 Business Prediction App\")\n",
        "    st.markdown(\"Predict your business success potential instantly.\")\n",
        "    st.markdown(\"---\")\n",
        "    st.subheader(\"🌐 Connect With Me\")\n",
        "    st.write(\"Instagram: [@nbjoshua6](https://instagram.com/nbjoshua6)\")\n",
        "    st.write(\"🌍 [Website](https://faithconncthub.store)\")\n",
        "    st.write(\"📩 nbjoshua8@gmail.com\")\n",
        "    st.write(\"📞 +233 556 231 984\")\n",
        "    st.write(\"❤️ [Support or Donate](https://selar.com/showlove/nbjoshua)\")\n",
        "    st.markdown(\"---\")\n",
        "    st.caption(\"© 2025 NB Joshua | All Rights Reserved\")\n",
        "\n",
        "# ---- LOGIN SYSTEM ----\n",
        "names = [\"NB Joshua\", \"Premium User\"]\n",
        "usernames_list = [\"admin\", \"premium\"]\n",
        "passwords = [\"12345\", \"PREMIUM2025\"]\n",
        "\n",
        "# Create the credentials dictionary as expected by streamlit_authenticator\n",
        "credentials = {\n",
        "    \"usernames\": {\n",
        "        usernames_list[i]: {\"name\": names[i], \"password\": passwords[i]}\n",
        "        for i in range(len(usernames_list))\n",
        "    }\n",
        "}\n",
        "\n",
        "authenticator = stauth.Authenticate(credentials, \"business_app\", \"abcdef\", 30)\n",
        "name, auth_status, username = authenticator.login(\"Login\", \"main\")\n",
        "\n",
        "if auth_status:\n",
        "    authenticator.logout(\"Logout\", \"sidebar\")\n",
        "    st.sidebar.success(f\"✅ Logged in as: {name}\")\n",
        "\n",
        "    # ---- MAIN APP ----\n",
        "    st.title(\"🚀 Business Profile Prediction\")\n",
        "    st.write(\"Fill in the details below to predict your business success.\")\n",
        "\n",
        "    name_input = st.text_input(\"Business Name\")\n",
        "    industry = st.selectbox(\"Industry Type\", [\"Tech\", \"Fashion\", \"E-commerce\", \"Agriculture\", \"Other\"])\n",
        "    experience = st.slider(\"Years of Experience\", 0, 20)\n",
        "    marketing = st.slider(\"Marketing Budget (USD)\", 100, 10000)\n",
        "    risk = st.selectbox(\"Risk Level\", [\"Low\", \"Medium\", \"High\"])\n",
        "\n",
        "    if st.button(\"Predict\"):\n",
        "        if marketing > 5000 and risk == \"Low\":\n",
        "            result = \"High Success Potential 🚀\"\n",
        "        elif marketing > 2000:\n",
        "            result = \"Moderate Success Potential ⚡\"\n",
        "        else:\n",
        "            result = \"Needs Improvement 💡\"\n",
        "\n",
        "        st.success(f\"**Prediction Result:** {result}\")\n",
        "        st.download_button(\"📄 Download Result\", f\"Business: {name_input}\\nPrediction: {result}\", file_name=\"business_prediction.txt\")\n",
        "\n",
        "        # ---- PREMIUM FEATURES ----\n",
        "        if username == \"premium\":\n",
        "            st.markdown(\"---\")\n",
        "            st.subheader(\"🌟 Premium Insights\")\n",
        "            st.write(\"✅ Advanced analytics for market positioning\")\n",
        "            st.write(\"✅ Smart suggestions for scaling your business\")\n",
        "            st.write(\"✅ Personalized success roadmap\")\n",
        "        else:\n",
        "            st.markdown(\"---\")\n",
        "            st.warning(\"Upgrade to Premium for more insights and analytics.\")\n",
        "            st.markdown(\"👉 [Buy Premium Access on Selar](https://selar.com/showlove/nbjoshua)\")\n",
        "\n",
        "else:\n",
        "    if auth_status is False:\n",
        "        st.error(\"❌ Incorrect username or password.\")\n",
        "    elif auth_status is None:\n",
        "        st.warning(\"🔐 Please login to access the app.\")\n",
        "\n",
        "# ---- FOOTER ----\n",
        "st.markdown(\"---\")\n",
        "st.caption(\"Built with ❤️ by NB Joshua | Powered by Streamlit | [FaithConnctHub.store](https://faithconncthub.store)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "y6W4VtpNskbk",
        "outputId": "d25fd9ef-1f93-440d-bbd5-d5dda0e5628b"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-11-02 04:02:35.722 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.724 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.725 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.726 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.726 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.727 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.731 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.732 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.733 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.734 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.734 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.735 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.735 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.737 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.737 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.738 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.739 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.740 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.741 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.741 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.742 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.743 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.744 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.745 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.745 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.746 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.748 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.748 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.749 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.749 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.751 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.751 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.753 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.754 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.755 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.756 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.758 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:35.759 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.442 Session state does not function when running a script without `streamlit run`\n",
            "2025-11-02 04:02:36.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.445 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.449 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.453 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.457 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.462 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.462 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.463 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.465 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.466 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.467 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:02:36.469 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "Location must be one of 'main' or 'sidebar' or 'unrendered'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1297040467.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     45\u001b[0m \u001b[0mauthenticator\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstauth\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAuthenticate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcredentials\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"business_app\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"abcdef\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m30\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 46\u001b[0;31m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mauth_status\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0musername\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mauthenticator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Login\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"main\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     47\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mauth_status\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/streamlit_authenticator/views/authentication_view.py\u001b[0m in \u001b[0;36mlogin\u001b[0;34m(self, location, max_concurrent_users, max_login_attempts, fields, captcha, single_session, clear_on_submit, key, callback)\u001b[0m\n\u001b[1;32m    327\u001b[0m                       'Login':'Login', 'Captcha':'Captcha'}\n\u001b[1;32m    328\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlocation\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m'main'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'sidebar'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'unrendered'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 329\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Location must be one of 'main' or 'sidebar' or 'unrendered'\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    330\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_state\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'authentication_status'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    331\u001b[0m             \u001b[0mtoken\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcookie_controller\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_cookie\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: Location must be one of 'main' or 'sidebar' or 'unrendered'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hehBc9yXy_jp",
        "outputId": "d1395244-dcd7-48b4-9b0f-016d8c4c33d7"
      },
      "source": [
        "!pip install streamlit_authenticator"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit_authenticator in /usr/local/lib/python3.12/dist-packages (0.4.2)\n",
            "Requirement already satisfied: bcrypt>=3.1.7 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (5.0.0)\n",
            "Requirement already satisfied: captcha>=0.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (0.7.1)\n",
            "Requirement already satisfied: cryptography>=42.0.5 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (43.0.3)\n",
            "Requirement already satisfied: extra-streamlit-components>=0.1.70 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (0.1.81)\n",
            "Requirement already satisfied: PyJWT>=2.3.0 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (2.10.1)\n",
            "Requirement already satisfied: PyYAML>=5.3.1 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (6.0.3)\n",
            "Requirement already satisfied: streamlit>=1.37.0 in /usr/local/lib/python3.12/dist-packages (from streamlit_authenticator) (1.51.0)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.12/dist-packages (from captcha>=0.5.0->streamlit_authenticator) (11.3.0)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.12/dist-packages (from cryptography>=42.0.5->streamlit_authenticator) (2.0.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (8.3.0)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (2.0.2)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (25.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (2.2.2)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (5.29.5)\n",
            "Requirement already satisfied: pyarrow<22,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (3.1.45)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (0.9.1)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit>=1.37.0->streamlit_authenticator) (6.5.1)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (2.10.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.12/dist-packages (from cffi>=1.12->cryptography>=42.0.5->streamlit_authenticator) (2.23)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit>=1.37.0->streamlit_authenticator) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit>=1.37.0->streamlit_authenticator) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit>=1.37.0->streamlit_authenticator) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit>=1.37.0->streamlit_authenticator) (2025.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit>=1.37.0->streamlit_authenticator) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit>=1.37.0->streamlit_authenticator) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit>=1.37.0->streamlit_authenticator) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit>=1.37.0->streamlit_authenticator) (2025.10.5)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit>=1.37.0->streamlit_authenticator) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (25.4.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit>=1.37.0->streamlit_authenticator) (0.28.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit>=1.37.0->streamlit_authenticator) (1.17.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "streamlit\n",
        "streamlit-authenticator\n",
        "pyngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 183
        },
        "id": "7H-6Y_rFuheX",
        "outputId": "56a23c2d-54c5-4038-c3ea-62b3dcaae270"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'streamlit' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1548911725.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mstreamlit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mauthenticator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mpyngrok\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'streamlit' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# --- FULL BUSINESS APP (Ready Version) ---\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "\n",
        "# Page setup\n",
        "st.set_page_config(page_title=\"Business Profit Prediction\", layout=\"wide\")\n",
        "\n",
        "# Sidebar\n",
        "st.sidebar.title(\"📊 Business Profit App\")\n",
        "st.sidebar.markdown(\"Predict business profits easily and manage your data.\")\n",
        "menu = st.sidebar.radio(\"Navigation\", [\"Home\", \"About\", \"Premium\"])\n",
        "\n",
        "# --- HOME PAGE ---\n",
        "if menu == \"Home\":\n",
        "    st.title(\"💼 Business Profit Prediction App\")\n",
        "    st.write(\"This simple app predicts business profit using R&D, Administration, and Marketing Spend.\")\n",
        "\n",
        "    # Input section\n",
        "    rd = st.number_input(\"R&D Spend\", min_value=0.0, step=1000.0)\n",
        "    admin = st.number_input(\"Administration\", min_value=0.0, step=1000.0)\n",
        "    marketing = st.number_input(\"Marketing Spend\", min_value=0.0, step=1000.0)\n",
        "\n",
        "    if st.button(\"Predict Profit\"):\n",
        "        result = (rd * 0.6) + (admin * 0.3) + (marketing * 0.5)\n",
        "        st.success(f\"Predicted Profit: ${result:,.2f}\")\n",
        "\n",
        "    # Upload section\n",
        "    st.subheader(\"Upload Your CSV Data (Optional)\")\n",
        "    uploaded_file = st.file_uploader(\"Upload CSV with R&D, Administration, Marketing, Profit\", type=[\"csv\"])\n",
        "    if uploaded_file is not None:\n",
        "        data = pd.read_csv(uploaded_file)\n",
        "        st.dataframe(data.head())\n",
        "\n",
        "# --- ABOUT PAGE ---\n",
        "elif menu == \"About\":\n",
        "    st.title(\"ℹ️ About This App\")\n",
        "    st.markdown(\"\"\"\n",
        "    This app helps business owners predict potential profit\n",
        "    based on their R&D, Administration, and Marketing spend.\n",
        "\n",
        "    **Creator:** Nb Joshua\n",
        "    **Instagram:** [@nbjoshua6](https://instagram.com/nbjoshua6)\n",
        "    **Website:** [faithconncthub.store](https://faithconncthub.store)\n",
        "    **Email:** nbjoshua8@gmail.com\n",
        "    **Phone:** +233556231984\n",
        "    \"\"\")\n",
        "\n",
        "# --- PREMIUM PAGE ---\n",
        "elif menu == \"Premium\":\n",
        "    st.title(\"🚀 Premium Access\")\n",
        "    st.write(\"Unlock advanced features and unlimited predictions.\")\n",
        "    st.markdown(\"[Buy Premium on Selar](https://selar.com/showlove/nbjoshua)\")\n",
        "\n",
        "    code = st.text_input(\"Enter Premium Access Code\")\n",
        "    if st.button(\"Unlock\"):\n",
        "        if code.strip().upper() == \"PREMIUM2025\":\n",
        "            st.success(\"✅ Premium Unlocked! Enjoy your access.\")\n",
        "        else:\n",
        "            st.error(\"❌ Invalid Code. Purchase Premium from the link above.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FN05W7sy0Olm",
        "outputId": "443addbb-2849-49e7-cd3d-d7625f0a986f"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-11-02 04:26:34.674 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.675 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.676 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.678 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.679 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.680 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.681 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.682 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.683 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.685 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.690 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.691 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.693 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.696 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.696 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.699 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.700 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.703 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.705 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.706 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.707 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.709 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.710 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.711 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.712 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.714 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.716 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.716 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.717 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.718 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.719 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.721 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.721 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.723 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.725 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.726 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.727 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.731 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.732 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.732 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.734 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.735 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.736 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.736 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.738 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.740 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.741 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.742 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.743 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-11-02 04:26:34.744 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}