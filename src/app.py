from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from config import STATIC_PATH

from database.database import get_session
from database.models import Class, Group
from src.external import get_schedule

app = FastAPI()


@app.get("/schedule")
async def schedule(facility_name: str = None,
                   group_name: str = None,
                   session: AsyncSession = Depends(get_session)):
    
    if facility_name != None and group_name == None:
        
        facility_raw = (await session.execute(
            select(Class.num)
            .where(Class.name == facility_name)
            .filter(Class.name.ilike('%' + facility_name + '%'))
        )).first()
        
        if facility_raw == None:
            raise HTTPException(status_code=400, detail="facility not found")
        
        facility_id = facility_raw._mapping["num"]
        
        return await get_schedule(facility=facility_id)
    
    elif facility_name == None and group_name != None:
        
        group_raw = (await session.execute(
            select(Group.num).where(Group.name == group_name)
        )).first()
        
        if group_raw == None:
            raise HTTPException(status_code=400, detail="group not found")
        
        group_id = group_raw._mapping["num"]
        
        return await get_schedule(group=group_id)
    
    else:
        raise HTTPException(status_code=400, detail="only one param should be used")


@app.get("/install_gropus")
async def install_gropus(session: AsyncSession = Depends(get_session)):
    
    file = open(f"{STATIC_PATH}/groups.txt")
    
    groups = [(int(x[0].replace('"', '')), x[1].replace('\n', '')) for x in [x.split(">") for x in file.readlines()]]
    
    for group in groups:
        
        group_insert = {
            "name": group[1],
            "num": group[0]
        }
        
        await session.execute(insert(Group).values(group_insert))
        await session.commit()
    
    return {"detail": "groups install success"}


@app.get("/install_classes")
async def install_classes(session: AsyncSession = Depends(get_session)):
    
    file = open(f"{STATIC_PATH}/classes.txt")
    
    groups = [(int(x[0].replace('"', '')), x[1].replace('\n', '')) for x in [x.split(">") for x in file.readlines()]]
    
    for group in groups:
        
        group_insert = {
            "name": group[1],
            "num": group[0]
        }
        
        await session.execute(insert(Class).values(group_insert))
        await session.commit()
    
    return {"detail": "classes install success"}