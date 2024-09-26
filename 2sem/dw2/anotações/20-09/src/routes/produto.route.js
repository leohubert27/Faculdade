import { Router } from 'express'
import ProdutoController from '../controllers/produto.controller.js'
import { ProdutoValidator, produtoUpdateValidator, produtoIdValidator } from '../validators/produto.validator.js'

const router = Router()

router.get('/', ProdutoController.index)
router.post('/', ProdutoValidator ,ProdutoController.create)
router.get('/:id', produtoIdValidator,ProdutoController.show)
router.put ('/:id', produtoUpdateValidator,ProdutoController.delete)
router.delete ('/:id', produtoIdValidator, ProdutoController)

export default router