package fichesingredients

//Les Fiches des Ingrédients Vectorisation

//Fiche Requête Utilisateur
type RequeteUtilisateur struct {
	Contenu string
}

//Action:  avoir son Contenu
func (r *RequeteUtilisateur)AvoirContenu()string{
	return r.Contenu
}

//Fiche Fichier Arrivé
type FichierArriver struct {
	Contenu string
	Size int
}

//Action: Avoir son Contenu
func (f *FichierArriver)AvoirContenu()string{
	if f.Size > 0 {

	return f.Contenu
	}
	return "Fichier vide"
}

//Action: Avoir sa taille
func (f *FichierArriver)AvoirTaille()int{
	return f.Size
}


//Fiche Vecteur
type Vecteur struct {
	Longueur int
	Dimension int
	Valeurs []float64
}


//Action sur le Vecteur: avoir les valeurs
func (vec *Vecteur)AvoirValeurs()([]float64){
	return vec.Valeurs
}

//Action sur le vecteur: avoir la dimension
func(vec *Vecteur)AvoirDimension()(int){
	return vec.Dimension
}

//Action sur le vecteur: avoir la Longueur
func(vec *Vecteur)AvoirLongeur()(int){
	return vec.Longueur
}
