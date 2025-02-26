<img align="center" width="453" alt="logoPharma" src="https://github.com/Team-Upsilon/PharmaVerse-frontend/assets/103581884/6c562eb4-4c57-4f20-9cdd-e9fe98cc27f1">



# 🌿 PharmaVerse – Decentralized Medical Ecosystem

PharmaVerse is a **decentralized blockchain application** designed to streamline **medicine production, tracking, and verification**. This project utilizes **blockchain technology and smart contracts** to ensure **transparency and accountability** throughout the pharmaceutical supply chain. The system integrates a **frontend interface, backend infrastructure, and AI-powered chatbot** for seamless interactions with blockchain records.

---

## 🚀 Features  

✅ **Decentralized Medicine Tracking** – Ensures transparency and security in drug manufacturing and distribution.  
✅ **Smart Contracts** – Eight Solidity-based contracts manage **raw materials, quality inspection, batch scheduling, and distribution**.  
✅ **Automated Batch Scheduling** – Optimized production workflows using **smart contract logic**.  
✅ **AI Chatbot Assistant** – Google AI Studio-powered chatbot **guides users through PharmaVerse interactions**.  
✅ **Web3 & MetaMask Support** – **Secure Ethereum transactions** with blockchain-based authentication.  
✅ **Testing Framework** – Uses **Chai and Mocha** for **smart contract testing**.  
✅ **Deployment** – Contracts are deployed on the **Sepolia Testnet using Hardhat**.  

---

## 🛠️ Getting Started  

### 1️⃣ Prerequisites  

Before setting up the project, ensure you have:  

- **[Node.js (v16 or later)](https://nodejs.org/)** – Required for running both frontend and backend.  
- **[MetaMask](https://metamask.io/)** – To connect with the **Ethereum Sepolia Testnet**.  
- **PharmaVerse Smart Contracts** – Already deployed on **Sepolia Testnet**.  
- **Alchemy or Infura API Key** – For blockchain RPC access.  
- **Hardhat** – Ethereum development environment.  

---

## 📌 Frontend Setup  

### 2️⃣ Clone the Repository  

```sh
 git clone https://github.com/yourusername/pharmaverse-frontend.git
 cd pharmaverse-frontend
```

### 3️⃣ Install Dependencies  

```sh
 npm install
```

### 4️⃣ Configure Environment Variables  

Create a **.env** file in the project root and add the required keys:  

```sh
 REACT_APP_BLOCKCHAIN_RPC_URL=<your_rpc_provider_url>
 REACT_APP_CONTRACT_ADDRESS=<your_smart_contract_address>
 REACT_APP_AI_CHATBOT_API=<your_google_ai_studio_api_key>
```

### 5️⃣ Run the Application  

Start the development server:  

```sh
 npm start
```

The application will be available at **http://localhost:3000**.  

---

## 🔄 Backend Setup  

### 6️⃣ Clone the Backend Repository  

```sh
 git clone https://github.com/yourusername/pharmaverse-backend.git
 cd pharmaverse-backend
```

### 7️⃣ Install Dependencies  

```sh
 npm install
```

### 8️⃣ Configure Environment Variables  

Create a **.env** file in the project root and add the following:  

```sh
 PRIVATE_KEY=<your_wallet_private_key>
 ALCHEMY_API_URL=<your_alchemy_or_infura_url>
```

### 9️⃣ Compile Smart Contracts  

```sh
 npx hardhat compile
```

### 🔟 Run Tests  

```sh
 npx hardhat test
```

### 1️⃣1️⃣ Deploy to Sepolia Testnet  

```sh
 npx hardhat run scripts/deploy.js --network sepolia
```

### 1️⃣2️⃣ Verify Contract on Etherscan (Optional)  

```sh
 npx hardhat verify --network sepolia <contract_address>
```

---

## 🔐 Security Considerations  

- **API keys and sensitive data should NEVER be committed to GitHub**.  
- **Use HTTPS** to encrypt communications and protect user data.  
- **Ensure MetaMask permissions are properly managed** to prevent unauthorized blockchain transactions.  
- **Role-Based Access Control (RBAC)** is implemented to restrict unauthorized actions.  

---

## 📩 Contact  

For any issues or clarifications, reach out to the project owner.  

---

Now your **PharmaVerse frontend and backend** are **ready for development, deployment, and submission**! 🚀

For any issues or clarifications, reach out to the project owner.  

Manasvi Khatri:9479909805
manasviks16@gmail.com


UI screenshots :-
![image](https://github.com/user-attachments/assets/76429222-30f3-453b-b3f7-7decb568bf1e)
![image](https://github.com/user-attachments/assets/7fef9003-44b4-43af-acf1-a3524c3a7439)
![image](https://github.com/user-attachments/assets/274f3a1d-21b6-4d63-ae7b-1b20d7a98c2e)
![image](https://github.com/user-attachments/assets/5763f8b0-d5fc-4ead-b6bd-941c98198bbc)
![image](https://github.com/user-attachments/assets/42848988-6637-49f8-9271-dd5fe1f7e114)
![image](https://github.com/user-attachments/assets/857e58df-07bc-4b14-9ca4-448b87debf58)
![image](https://github.com/user-attachments/assets/07c27fc3-1070-4ccc-96ad-93c11724aab2)
![image](https://github.com/user-attachments/assets/3fa4d110-45ff-496c-9394-feb970eb4465)
![image](https://github.com/user-attachments/assets/6d6a5deb-d561-47e2-8b1f-59bf9228d602)
![image](https://github.com/user-attachments/assets/0acf2fe4-3e40-4a1b-b41c-0bc3f0b7d9c9)
![image](https://github.com/user-attachments/assets/647e799f-042b-41eb-abc7-4a11d1f96491)
![image](https://github.com/user-attachments/assets/407d25c9-fba0-4d6e-a922-04cac80c69ac)
![image](https://github.com/user-attachments/assets/a3bc4432-78b2-4e06-88fc-1abd256422fb)
![image](https://github.com/user-attachments/assets/58b27c76-fbb4-4e3a-8319-d4f4279e5bc7)
![image](https://github.com/user-attachments/assets/e2cc8461-78de-454e-9a57-906516c57648)
![image](https://github.com/user-attachments/assets/fc16a315-82d5-48f9-b617-1d59b6a6dcc5)
![image](https://github.com/user-attachments/assets/717251e4-cb01-4381-90c3-ca76a0bb500d)
![image](https://github.com/user-attachments/assets/3b45cf7e-1eca-46be-bfc4-e775682601e5)
![image](https://github.com/user-attachments/assets/bd09f277-f8f6-4a09-8791-f3c28d652753)
![image](https://github.com/user-attachments/assets/29b19220-df79-4933-a907-5f9e00178c5d)
![image](https://github.com/user-attachments/assets/1fb51d9e-3714-4dc2-962e-311cce1f7481)
![image](https://github.com/user-attachments/assets/a94c941a-ed7e-4022-beac-7416e0573dc2)
![image](https://github.com/user-attachments/assets/b69cc602-44e3-475e-9d60-a98a7295bc7d)






























