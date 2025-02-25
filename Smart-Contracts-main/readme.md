# 🌿 PharmaVerse Backend – Decentralized Medical Ecosystem

PharmaVerse is a **decentralized blockchain-based application** that enhances **medicine production, tracking, and verification**. This backend handles **smart contract interactions, blockchain data management, and AI chatbot integration**, ensuring seamless communication between the **frontend, blockchain, and AI-powered assistant**.

---

## 🚀 Features  

✅ **Smart Contract Management** – Facilitates **batch scheduling, raw material tracking, and quality inspection**.  
✅ **Web3 Blockchain Interaction** – Enables secure **Ethereum transactions** via the **Sepolia Testnet**.  
✅ **AI Chatbot API** – Supports Google AI Studio-based chatbot for **user guidance and automation**.  
✅ **Testing & Deployment** – Uses **Chai, Mocha, and Hardhat** for **unit testing and deployment**.  
✅ **Secure API** – Provides **backend endpoints for querying blockchain data** and executing transactions.  

---

## 🛠️ Getting Started  

### 1️⃣ Prerequisites  

Ensure you have the following installed:  

- **[Node.js (v16 or later)](https://nodejs.org/)** – Required for backend services.  
- **[Hardhat](https://hardhat.org/)** – Ethereum development framework.  
- **[MetaMask](https://metamask.io/)** – For smart contract interaction.  
- **Alchemy or Infura API Key** – For blockchain RPC access.  

---

## 📌 Backend Setup  

### 2️⃣ Clone the Repository  

```sh
 git clone https://github.com/yourusername/pharmaverse-backend.git
 cd pharmaverse-backend
```

### 3️⃣ Install Dependencies  

```sh
 npm install
```

### 4️⃣ Configure Environment Variables  

Create a **.env** file in the project root and add the required keys:  

```sh
 PRIVATE_KEY=<your_wallet_private_key>
 ALCHEMY_API_URL=<your_alchemy_or_infura_url>
```

### 5️⃣ Compile Smart Contracts  

```sh
 npx hardhat compile
```

### 6️⃣ Run Tests  

```sh
 npx hardhat test
```

### 7️⃣ Deploy to Sepolia Testnet  

```sh
 npx hardhat run scripts/deploy.js --network sepolia
```

### 8️⃣ Verify Smart Contracts on Etherscan (Optional)  

```sh
 npx hardhat verify --network sepolia <contract_address>
```

---

## 🔄 AI Chatbot Integration  

The backend integrates **Google AI Studio’s NLP models** to provide a **custom AI chatbot** for guiding users through **smart contract interactions**.  

### 🔹 Chatbot Capabilities:  
- **Role-Based Guidance** – Assists **manufacturers, suppliers, and pharmacists** in interacting with PharmaVerse.  
- **Blockchain Queries** – Fetches **batch details, quality grades, and inventory** from the blockchain.  
- **Automated Smart Contract Execution** – AI can trigger **batch scheduling, verification, and compliance checks**.  

### 9️⃣ Configure Chatbot Environment Variables  

```sh
 REACT_APP_AI_CHATBOT_API=<your_google_ai_studio_api_key>
```

---

## 🔐 Security Considerations  

- **Never expose private keys in public repositories**.  
- **Enforce Role-Based Access Control (RBAC)** to prevent unauthorized actions.  
- **Use HTTPS** to secure backend API communications.  

---

## 📩 Contact  

For any issues or clarifications, reach out to the project owner.  

---

Now your **PharmaVerse backend** is **ready for deployment and AI-powered smart contract execution! 🚀**
