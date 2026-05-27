package fichesingredients

// Fiches ingrédients model de vectorisation

//Fiche Model

type Model struct {
	Nom string
	Taille int
	Entree string
	FenetreContexte int
	Sortie []float64
}

//Action Model

func (m *Model)AvoirNom()string{
	return m.Nom
}

func (m *Model)AvoirTaille()int{
	return m.Taille
}

func (m *Model)AvoirFenetreContexte()int{
	return m.FenetreContexte
}

// func (m *Model)Vectorisation(s string)[]float64{
// 	m.Entree = s
// 	// envoyer la chaine de caractère au model d'IA
// 	// Il faut l'envoyer via un chemin  au service IA


// }
