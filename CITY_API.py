from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle d'une ville
class Ville(BaseModel):
    nom: str
    population: int
    region: str

# Base de données fictive
villes = {
    1: Ville(nom="Abidjan", population=5000000, region="Lagunes"),
    2: Ville(nom="Yamoussoukro", population=350000, region="Lacs"),
}

# GET toutes les villes
@app.get("/villes")
def get_villes():
    return villes

# GET une ville par ID
@app.get("/villes/{ville_id}")
def get_ville(ville_id: int):
    if ville_id not in villes:
        raise HTTPException(status_code=404, detail="Ville non trouvée")
    return villes[ville_id]

# POST pour ajouter une ville
@app.post("/villes")
def ajouter_ville(ville: Ville):
    new_id = max(villes.keys()) + 1
    villes[new_id] = ville
    return {"id": new_id, "ville": ville}

# PUT pour modifier une ville
@app.put("/villes/{ville_id}")
def modifier_ville(ville_id: int, ville: Ville):
    if ville_id not in villes:
        raise HTTPException(status_code=404, detail="Ville non trouvée")
    villes[ville_id] = ville
    return ville

# DELETE pour supprimer une ville
@app.delete("/villes/{ville_id}")
def supprimer_ville(ville_id: int):
    if ville_id not in villes:
        raise HTTPException(status_code=404, detail="Ville non trouvée")
    del villes[ville_id]
    return {"message": "Ville supprimée"}
