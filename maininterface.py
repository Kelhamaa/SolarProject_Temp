from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from predictmodels.modelsusepymatgenobject import sta_predict, bandgap_predict
from database import *

maininterface=APIRouter()

template = Jinja2Templates(directory="template")
@maininterface.get("/getpymatgenobject")
async def get_pymatgen_object(request: Request):

    return template.TemplateResponse(
        "inputusepymatgenobject.html",
        {
            "request": request
        }
    )
@maininterface.post("/allprediction")
async def all_prediction(request: Request,element_1: str= Form(), element_2: str= Form(), element_3: str= Form(),
                       abc_str: str= Form(), angles_str: str= Form(), volume: float= Form(),
                       matrix_str: str= Form(), pbc_str: str = Form(),
                       frac_coords_1_str: str = Form(),
                       frac_coords_2_str: str = Form(),
                       frac_coords_3_str: str = Form(),
                       frac_coords_4_str: str = Form(),
                       frac_coords_5_str: str = Form()):
    abc=[float(x) for x in abc_str.split(',')]
    angles=[float(x) for x in angles_str.split(',')]
    matrix_float = [float(x) for x in matrix_str.split(',')]
    matrix=[[matrix_float[0],matrix_float[1],matrix_float[2]],
            [matrix_float[3],matrix_float[4],matrix_float[5]],
            [matrix_float[6],matrix_float[7],matrix_float[8]]]

    pbc = [x for x in pbc_str.split(',')]
    frac_coords_1 = [float(x) for x in frac_coords_1_str.split(',')]
    frac_coords_2 = [float(x) for x in frac_coords_2_str.split(',')]
    frac_coords_3 = [float(x) for x in frac_coords_3_str.split(',')]
    frac_coords_4 = [float(x) for x in frac_coords_4_str.split(',')]
    frac_coords_5 = [float(x) for x in frac_coords_5_str.split(',')]
    stability=sta_predict(element_1,element_2,element_3,
                abc,angles,volume,matrix,pbc,
                frac_coords_1,frac_coords_2,frac_coords_3,frac_coords_4,frac_coords_5)
    bandgap=bandgap_predict(element_1,element_2,element_3,
                abc,angles,volume,matrix,pbc,
                frac_coords_1,frac_coords_2,frac_coords_3,frac_coords_4,frac_coords_5)
    pymatgenobject= await pymatgenobjectindb.create(
        element1=element_1,
        element2=element_2,
        element3=element_3,
        abc=abc_str,
        angles=angles_str,
        volume=volume,
        matrix=matrix_str,
        pbc=pbc_str,
        frac_coords_1=frac_coords_1_str,
        frac_coords_2=frac_coords_2_str,
        frac_coords_3=frac_coords_3_str,
        frac_coords_4=frac_coords_4_str,
        frac_coords_5=frac_coords_5_str,
        stability=stability,
        bandgap=bandgap

    )

    return template.TemplateResponse(
        "allprediction.html",
        {
            "request": request,
            ## fastapi doesn't support serialization of NumPy arrays directly. Convert into list before return it.
            "rf_bandgap": bandgap.tolist(),
            "rf_stability": stability.tolist()
        }
    )


@maininterface.get("/allobjectsindb")
async def get_all_objects(request:Request):
    try:
        objects = await pymatgenobjectindb.all()
        if not pymatgenobjectindb:
            return "No objects found"

        return template.TemplateResponse(
            "objects.html",
            {
                "request": request,
                "objects": objects
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

