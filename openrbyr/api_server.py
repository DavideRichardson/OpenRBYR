# api_server.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from openrbyr import ray_simulation, reconstruction

app = FastAPI()

class SimulationRequest(BaseModel):
    num_rays: int
    detector_distance: float

class ReconstructionRequest(BaseModel):
    projections: list

@app.get("/")
def read_root():
    return {"message": "Welcome to the OpenRBYR API!"}

@app.post("/simulate_rays")
def simulate_rays(request: SimulationRequest):
    sim = ray_simulation.RaySimulation(request.num_rays, request.detector_distance)
    rays = sim.simulate_rays()
    return {"rays": rays}

@app.post("/reconstruct")
def reconstruct_image(request: ReconstructionRequest):
    recon = reconstruction.MARTReconstruction()
    reconstructed = recon.reconstruct(np.array(request.projections))
    return {"reconstructed_image": reconstructed.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
