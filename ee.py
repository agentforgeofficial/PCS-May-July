raw_data = {
    "status": "success",
    "data": {
        "agent_name": "Neon_Viper",
        "system_status": "Active",
        "inventory": ["lockpick", "decryption_key", " EMP_grenade"],
        "location": {"lat": 34.0522, "lon": -118.2437, "city": "Los Santos"}
    }
}

name = raw_data["data"]["location"]["city"]
print(name)