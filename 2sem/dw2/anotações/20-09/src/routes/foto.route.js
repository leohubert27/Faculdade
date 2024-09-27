import { Router } from 'express'
import FotoController from '../controllers/foto.controller.js'
import { fotoValidator, fotoUpdateValidator, fotoIdValidator } from '../validators/foto.validator.js'

const router = Router()

router.get('/', FotoController.index)
router.post('/', fotoValidator ,FotoController.create)
//router.get('/:id', produtoIdValidator,FotoController.show)
//router.put ('/:id', produtoUpdateValidator,FotoController.delete)
//router.delete ('/:id', produtoIdValidator, FotoController)

export default router